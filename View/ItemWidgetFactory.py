from abc import ABC, abstractmethod
from ItemWidget import ItemWidget
from StoreItemWidget import StoreItemWidget
from LibraryItemWidget import LibraryItemWidget

class ItemWidgetFactory(ABC):

    def createItemWidget(WidgetType):
        
        itemWidget = None

        if (WidgetType == "store") :
            itemWidget = StoreItemWidget()
        elif (WidgetType == "library"):
            itemWidget = LibraryItemWidget()

        return itemWidget