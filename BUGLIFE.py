import operator

rawlist = []  # contains rawly imputed number of individual bugs and their separate interactions
ind_int = []  # input converted in to usable data
specifics = []  # specifics of each interaction
specifics_ref = []  # refined specifics
interactions = 0
individuals = 0
amale = []
afemale = []
emptydict = {}

def scenarios():  # Scenario specifications input
    check = False
    while check is False:
        try:
            number_of_scenarios = int(input("Please input the number of scenarios:"))
            for i in range(0, number_of_scenarios):  #  Number of scenarios
                individuals_interactions(rawlist, ind_int)
                check = True
        except ValueError:
            print("Invalid input")


def individuals_interactions(rawlist, ind_int):  # Number of individuals and their interactions
    try:
        rawlist = input("Input number of bugs (up to 2000) and the enumeration of their interactions (up to 1000000) "
                        "separated by an empty space")
        ind_int = (rawlist.split(' '))  # input converted in to usable data
        if len(ind_int) == 2:
            individuals = int(ind_int[0])
            interactions = int(ind_int[1])
            if 1 <= individuals <= 2000 and 1 <= interactions <= 10000:
                scenario_specifications(amale, afemale, specifics, interactions)
    except ValueError:
        print("Ivalid input")


def scenario_specifications(amale, afemale, specifics, interactions):
    # Individual scenario specifications
    for i in range(0, interactions):
        specifics = input("Please input scenario specifics in the form of 'x y' where 'x' represents one "
                          "insect's number, and y represents the other insect's number")
        specifics_ref = specifics.split (' ')
        y = str(specifics_ref[0])
        x = str(specifics_ref[1])
        emptydict[x] = str(y)
        emptydict[y] = x
    sortdict = sorted(emptydict.items(), key=operator.itemgetter(0))
    print(sortdict)

"""
def scenario_specifications2 (amale, afemale, specifics, interactions):
    # Individual scenario specifications after the initial set
    for i in range(0, interactions):
        specifics = input("Please input scenario specifics in the form of 'x y' where 'x' represents one "
                          "insect's number, and y represents the other insect's number")
        specifics_ref = specifics.split (' ')
        y = str(specifics_ref[0])
        x = str(specifics_ref[1])
        amale.append(y)
        afemale.append(x)
"""


scenarios()
