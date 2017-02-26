class Boy:
    def __init__(vicky,name,attractiv,intel,budget,min_girlAttract):
        vicky.name=name
        vicky.attractiv=attractiv
        vicky.intel=intel
        vicky.budget=budget
        vicky.min_girlAttract=min_girlAttract
        vicky.type=''
        vicky.rstatus = 'single'
        vicky.happiness = 0
        vicky.girlfriend = ''
        vicky.budget=budget

    def checkElligible(vicky, girl):
        if (vicky.budget >= girl.budget and vicky.rstatus == 'single' and vicky.min_girlAttract >= girl.attractiv):
            return True
        return False
class Girl:
    girls_count = 0
    def __init__(girl, name, attractiv, intel, budget):
        girl.name = name
        girl.attractiv = attractiv
        girl.intel = intel
        girl.budget = budget
        girl.rstatus = 'single'
        girl.boyFriendName = ''
        girl.type=''
        girl.happinessLevel = 0
        Girl.girls_count += 1
    def checkElligible(girl, boy):
        if (girl.budget <= boy.budget and girl.rstatus == 'single'):
            return True
        return False