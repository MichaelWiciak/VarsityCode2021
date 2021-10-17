class ShoppingBag:

    def calculate_bag_total(self, items, discounts):
        # check items are correct format
        # do calculations
        if items == None:
            return 0
        for item in items:
            # get each item
            try:
                self.__checkLength(item,6)
                
                
                getFirstThreeCharacters = item[:3]
                if self.__checkAllLetters(getFirstThreeCharacters):
                    #All first three characters are True
                    getNextThreeCharacters = item[3:6]
                    
                    try:
                        self.__checkAllIntergers(getNextThreeCharacters)
                    except ValueError:
                        raise CodeError("Does not contain three interger code after letters, wrong code")
                    
                    
                    
                elif self.__checkAllLetters(getFirstThreeCharacters) == False:
                    # Not all characters are true, wrong item code, redo
                    #Do error handling here
                    raise CodeError("First three characters are not letters, wrong item code.")
                
                
                
            except CodeError:
                items.remove(item)
                continue
            ## ^^^^ Above checks correctly if each item code is of correct format
        

        counter = 0
        while counter <= (len(items)-1):
            aListOfAllMatchingItems = [i for i in items if i.startswith(items[counter][:3])]
            anotherCopy = [i for i in items if i.startswith(items[counter][:3])]
            if len(aListOfAllMatchingItems) > 1:
                COPYaListOfAllMatchingItems = aListOfAllMatchingItems
                COPYaListOfAllMatchingItems.remove(items[counter])
                if items[counter] in COPYaListOfAllMatchingItems:
                    pass
                else:
                    for i in anotherCopy:
                        
                        items.remove(i)
                    counter=-1
            counter +=1
            
                
        for discount in discounts:
            try:
                self.__checkLength(discount,7)
                getFirstThreeCharacters = discount[:3]
                if self.__checkAllLetters(getFirstThreeCharacters):
                    #All first three characters are True
                    getNextCharacter = discount[3]
                    try:
                        self.__isInterger(getNextCharacter)
                        if getNextCharacter == 0:
                            raise ValueError
                    except ValueError:
                        raise CodeError("Does not contain interger code after letters, wrong code")
                    
                    
                    getNextCharacter = discount[4]
                    if getNextCharacter == 'P' or 'C':
                        pass
                    else:
                        raise CodeError("Letter is not P or C")
                    
                    if self.__isLetter(getNextCharacter) == False:
                        raise CodeError("Characters is not a letter, wrong item code.")
                    
                    getNextCharacter = discount[5:7]
                    try:
                        self.__checkAllIntergers(getNextCharacter)
                    except ValueError:
                        raise CodeError("Does not contain interger code after letters, wrong code")
                        
                elif self.__checkAllLetters(getFirstThreeCharacters) == False:
                    # Not all characters are true, wrong item code, redo
                    #Do error handling here
                    raise CodeError("First three characters are not letters, wrong item code.")
            except CodeError:
                discounts.remove(discount)
                continue
            

            
        
        # check discounts are correct format
        # apply them
    
        
    
        ## check which discount codes are valid for these items
        
        validDiscounts = []
        ## getme all item codes

        for discount in discounts:
            itemCodes = []
            for i in items:
                itemCodes.append(i[:3])
            copyOfItemCodes = itemCodes
            itemCode = discount[:3]
            if itemCode in itemCodes:
                howManyItemsHaveToBeInBasketToAddDiscount = discount[3]
                isValid = True
                for x in range(int(howManyItemsHaveToBeInBasketToAddDiscount)):
                    if itemCode in copyOfItemCodes:
                        copyOfItemCodes.remove(itemCode)
                    else:
                        isValid = False
                        break
                
                if isValid:
                    
                    validDiscounts.append(discount)
        
        
        
        ### ^^ correctly classifies which discounts are valid for this transaction
        ## calculate cost below
        totalCost = 0

        for item in items:
            costOfItem = self.__getCostForItem(item)
            discountsForThisItem = [i for i in validDiscounts if i.startswith(item[:3])]
            if len(discountsForThisItem) == 0:
                costOfItem = self.__checkIfNegative(costOfItem)
                totalCost += costOfItem
            elif len(discountsForThisItem) == 1:
                discountType = self.__whatTypeOfDiscount(discountsForThisItem[0])
                magnitudeDiscount = self.__getMagnitudeOfDiscount(discountsForThisItem[0])
                aCost = self.__calculateCost(discountType, costOfItem, magnitudeDiscount)
                aCost = self.__checkIfNegative(aCost)
                totalCost += aCost
            elif len(discountsForThisItem) > 1:
                allPossibleCostsForThisItem = []
                for i in range(len(discountsForThisItem)):
                    discountType = self.__whatTypeOfDiscount(discountsForThisItem[i])
                    magnitudeDiscount = self.__getMagnitudeOfDiscount(discountsForThisItem[i])
                    aCost = self.__calculateCost(discountType, costOfItem, magnitudeDiscount)
                    aCost = self.__checkIfNegative(aCost)
                    allPossibleCostsForThisItem.append(aCost)
                allPossibleCostsForThisItem.sort()
                highestValue = allPossibleCostsForThisItem[0]
                totalCost += highestValue
        
        
        
        if totalCost <= 0:
            totalCost = 0.00
        
        totalCost = round(totalCost,2)
        return totalCost
        
    
    def __checkIfNegative(self, costOfItem):
        if costOfItem <=0:
            return 0
        else:
            return costOfItem
    
    def __calculateCost(self, DiscountType, costOfItem, magnitudeDiscount):
        
        if DiscountType == 'C':
            return float(costOfItem)-float(magnitudeDiscount)
        elif DiscountType == 'P':
            return float(costOfItem)*(((100-float(magnitudeDiscount))/100))
    
    def __whatTypeOfDiscount(self,string):
        return string[4].upper()
        
    def __getCostForItem(self,item):
        return int(item[3:6])
    
    def __getMagnitudeOfDiscount(self,string):
        return string[5:7]
    
    def __checkLength(self, string, length):
        if len(string) != length:
            raise CodeError("Item code is not the correct length")
            
    def __isLetter(self, string):
        letter = string.lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if letter in alphabet:
            return True
        else:
            return False
    
    def __checkAllLetters(self, string):
        flag = True
        for x in string:
            checker = False
            if self.__isLetter(x):
                checker = True
            elif self.__isLetter(x) == False:
                checker = False
            
            if checker == False:
                return False
        return True
    
    def __isInterger(self,string):
        return int(string)

    def __checkAllIntergers(self,string):
        for x in string:
            self.__isInterger(x)

class CodeError(Exception):
    def __init__(self, message):
        self.__message = message
    def toString(self):
        return (self.__message)
