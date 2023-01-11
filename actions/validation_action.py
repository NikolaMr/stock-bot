from typing import Text, Any, Dict

from rasa_sdk import Tracker, ValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from actions.disambiguation import NED

class ValidatePredefinedSlots(ValidationAction):

    def validate_stock_base(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate location value."""
        return {'stock_base': NED.get_ticker_symbol(slot_value)}

    def validate_stock_match(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate location value."""
        return {'stock_match': NED.get_ticker_symbol(slot_value)}
