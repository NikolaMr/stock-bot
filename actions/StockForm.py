from typing import Text, List, Optional, Dict, Any

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType, SlotSet

from actions.utils.stock_informer import StockInformer


class ValidateStockForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_stock_form"

    async def required_slots(
            self,
            domain_slots: List[Text],
            dispatcher: "CollectingDispatcher",
            tracker: "Tracker",
            domain: "DomainDict",
    ) -> List[Text]:
        required_slots = ['stock_base', 'buy_at_market_price']

        if not tracker.get_slot('buy_at_market_price'):
            required_slots.append('price')

        required_slots.append('buy_type')
        required_slots.append('amount')

        return required_slots

    async def next_requested_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[EventType]:
        res = await super().next_requested_slot(dispatcher, tracker, domain)
        if res:
            if res['value'] == 'buy_at_market_price':
                stock = tracker.get_slot('stock_base')
                stock_price = StockInformer.get_stock_price(stock)
                dispatcher.utter_message(text=f'Just to inform you, the current stock price is: {stock_price}$')
        return res


class ActionSubmitStockForm(Action):

    def name(self) -> Text:
        return "action_submit_stock_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        stock = tracker.get_slot('stock_base')
        price = tracker.get_slot('price')
        buy_type = tracker.get_slot('buy_type')
        amount = tracker.get_slot('amount')

        text = f'Just filed a quote for {amount}'

        if buy_type == 'shares':
            text = f'{text} share/s'
        else:
            text = f'{text}$ worth'

        if price:
            text = f'{text} of {stock.upper()} at the price of {price}$.'
        else:
            text = f'{text} of {stock.upper()} at market price.'

        dispatcher.utter_message(text=text)

        return ActionCancelStockForm.get_reset_events()


class ActionCancelStockForm(Action):

    def name(self) -> Text:
        return "action_cancel_stock_form"

    @staticmethod
    def get_reset_events():
        ret = []

        for slot_name in ['stock_base', 'buy_at_market_price', 'price', 'buy_type', 'amount']:
            ret.append(SlotSet(slot_name, None))

        return ret

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return ActionCancelStockForm.get_reset_events()
