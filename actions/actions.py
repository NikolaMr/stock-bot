# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.utils.stock_informer import StockInformer


class ActionGetStockPrice(Action):

    def name(self) -> Text:
        return "action_get_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stock = tracker.get_slot('stock_base')

        if not stock:
            dispatcher.utter_message(text='Haven\'t matched any stock ticker symbol. '
                                          'Please check if typo is present or try another ticker symbol.')
            return []

        stock_price = StockInformer.get_stock_price(stock)

        dispatcher.utter_message(text=f"The price of {stock.upper()} is {stock_price:,}")

        return []


class ActionGetStocksCompared(Action):

    def name(self) -> Text:
        return "action_get_stocks_compared"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stock_base = tracker.get_slot('stock_base')
        stock_match = tracker.get_slot('stock_match')

        if not stock_base or not stock_match:
            dispatcher.utter_message(text='Haven\'t matched any stock ticker symbol. '
                                          'Please check if typo is present or try another ticker symbol.')
            return []

        stock_price_base = 12
        stock_price_match = 10

        dispatcher.utter_message(text=f"The price of {stock_base.upper()} increased "
                                      f"{stock_price_base - stock_price_match}% more "
                                      f"than the price of {stock_match.upper()}")

        return []


class ActionGetStockDetails(Action):

    def name(self) -> Text:
        return "action_get_stock_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        stock = tracker.get_slot('stock_base')

        if not stock:
            dispatcher.utter_message(text='Haven\'t matched any stock ticker symbol. '
                                          'Please check if typo is present or try another ticker symbol.')
            return []

        details = StockInformer.get_stock_details(stock)

        current_price = details['price']
        cnt_shares = details['number_of_shares']
        industry = details['industry']
        recommendation_status = details['recommendation_status']
        short_name = details['short_name']

        dispatcher.utter_message(text=f"{short_name}\n"
                                      f"Industry: {industry}\n"
                                      f"Current price: {current_price}$\n"
                                      f"Recommendation status: {recommendation_status}\n"
                                      f"Number of shares: {cnt_shares}")

        return []
