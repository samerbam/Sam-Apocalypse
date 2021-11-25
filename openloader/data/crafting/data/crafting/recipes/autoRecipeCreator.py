import json
import csv


"""
Machine	Type	Shaped Crafting	Multiple Ingredients	Additional Parameter
Millstone	create:milling	No	No	processingTime<ticks>
Crushing Wheel	create:crushing	No	No	processingTime<ticks>
Mechanical Press	create:pressing	No	No	
Mechnical Mixer	create:mixing	No	Yes	For ingredients: return_chance <double>, 1.0 = 100% {"item": "minecraft:blaze_rod", "return_chance": 0.97 }
Mechinal Press + Basin (Compacting)	crafting_shaped, crafting_shapeless	Yes	No	The Compacting looks for squared shaped recipes with the same items
Mechanical Sawing	create:cutting	No	No	processing_time<ticks>
Mechanical Cutting	minecraft:stonecutting	No	No	
Encased Fan + Water	create:splashing	No	No	
Encased Fan + Lava	minecraft:smelting	No	No	cookingtime<ticks>, experience<double>
Encased Fan + Fire/Campfire	minecraft:smoking	No	No	cookingtime<ticks>, experience<double>
Sandpaper Polishing	create:sandpaper_polishing	No	No	
Mechanical Crafter	create:mechanical_crafting	Yes	Yes	Shaped Crafting is needed
"""

RECIPE_TYPES = {
	1: "create:milling",
	2: "create:crushing",
	3: "create:pressing",
	4: "create:mixing",
	5: "create:cutting",
	6: "create:splashing",
	7: "create:mechanical_crafting",
	8: "create:sequenced_assembly",
	9: "create:emptying",
	10: "create:filling",
	11: "create:deploying"
}


def type1Recipe(rt, special="processingTime", fluid=True, chance=True):

	localOutput = {}

	checkList = ["item", "tag"]
	if fluid:
		checkList.append("fluid")
		checkList.append("fluidTag")

	localOutput["type"] = rt
	localOutput["ingredients"] = []
	localOutput["results"] = []

	asking_for_input = True

	step = 0
	while (asking_for_input):

		match step:
			case 0:
				print(f"Current Ingredients: {localOutput['ingredients']}")

				current_recipe = {}
				r_type = ""
				while (not (r_type in checkList)):
					r_type = input(f"Item type {' | '.join(checkList)} (item) ") or "item"

				item = input(f"Item or Tag ('') ") or ""

				current_recipe[r_type] = item

				if r_type == "fluid" or r_type == "fluidTag":
					amount = int(input("Fluid Amount (1000) ") or 1000)
					current_recipe["amount"] = amount


				localOutput["ingredients"].append(current_recipe)
				print(localOutput["ingredients"])
				check = input(f"Add another ingredient? [yes | NO] ")
				if not (check.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']):
					step += 1
			case 1:
				print(f"Current Results: {localOutput['results']}")

				current_recipe = {}
				r_type = ""
				while (not (r_type in checkList)):
					r_type = input(f"Item type {' | '.join(checkList)} (item) ") or "item"

				item = input(f"Item or Tag ('') ") or ""

				current_recipe[r_type] = item

				if r_type == "fluid" or r_type == "fluidTag":
					count = int(input("Fluid Amount (1000) ") or 1000)
				else:
					count = int(input("Item Count (1) ") or 1)

				current_recipe["count"] = count

				if chance:
					chance = float(input("Chance (1.0)") or 1.0)
					current_recipe["chance"] = chance


				localOutput["results"].append(current_recipe)
				print(localOutput["results"])
				check = input(f"Add another result? [yes | NO] ")
				if not (check.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']):
					step += 1
			case 2:
				if not (special == ""):
					localOutput[special] = input(f"{special} ('') ") or ''
				asking_for_input = False
				print(localOutput)
				return localOutput


# def mechanical_crafting():
# 	pass

# def sequenced_assembly():
# 	localOutput = {}

# 	localOutput["type"] = "create:sequenced_assembly"
# 	localOutput["ingredient"] = {} #only one item or tag.
# 	localOutput["transitionalItem"] = {} #only one item.
# 	localOutput["sequence"] = [] #multiple calls of main() appended into here, limited to specific types.
# 	localOutput["results"] = [] #with count & chance, item only.
# 	localOutput["loops"] = 1 #defualt to 1, change to any number > 0. Probably also has a max, not sure.


# 	def get_item_input(checkList, msg=''):
# 		# checkList = ["item", "tag"]
# 		r_type = ""
# 		while (not (r_type in checkList)):
# 			r_type = input(f"[{msg}] Item type {' | '.join(checkList)} (item) ") or "item"

# 		item = input(f"[{msg}] Item or Tag ('') ") or ""
# 		return {r_type: item}

# 	print('hmm')
# 	localOutput["ingredient"] = get_item_input(checkList=["item", "tag"], msg='ingredient')
# 	localOutput["transitionalItem"] = get_item_input(checkList=["item"], msg='transitionalItem')
# 	print('ugh')

# 	asking_for_input = True
# 	step = 0
# 	while (asking_for_input):

# 		match step:
# 			case 0:
# 				res = main()
# 				if (res):
# 					localOutput["sequence"].append(res)

# 				check = input(f"Add another step? [yes | NO] ")
# 				if not (check.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']):
# 					step += 1
# 			case 1:
# 				curItem = get_item_input(["item", "tag"], msg='result')
# 				curItem["count"] = int(input("[result] Item Count (1) ") or 1)
# 				curItem["chance"] = float(input("[result] Chance (1.0)") or 1.0)
# 				localOutput["results"].append(curItem)

# 				check = input(f"Add another step? [yes | NO] ")
# 				if not (check.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']):
# 					step += 1
# 			case 2:
# 				localOutput["loops"] = int(input("Loop Count (1) ") or 1)
# 				asking_for_input = False
# 				print(localOutput)
# 				return localOutput

				

# def main():

# 	chosen_type = input(f"Which recipe type options: {RECIPE_TYPES} : ")

# 	# if not (chosen_type in [str(x) for x in RECIPE_TYPES.keys()] or chosen_type in [str(x) for x in RECIPE_TYPES.values()]):
# 		# print('Invalid Recipe Type.')
# 		# return

# 	match chosen_type:
# 		case "1" | "create:milling":
# 			return type1Recipe("create:milling", special="processingTime", fluid=True, chance=True)
# 		case "2" | "create:crushing":
# 			return type1Recipe("create:crushing", special="processingTime", fluid=True, chance=True)
# 		case "3" | "create:pressing":
# 			return type1Recipe("create:pressing", special="", fluid=False, chance=False)
# 		case "4" | "create:mixing":
# 			return type1Recipe("create:mixing", special="heatRequirement", fluid=True, chance=False)
# 		case "5" | "create:cutting":
# 			return type1Recipe("create:cutting", special="processingTime", fluid=False, chance=False)
# 		case "6" | "create:splashing":
# 			return type1Recipe("create:splashing", special="", fluid=False, chance=True)
# 		case "7" | "create:mechanical_crafting":
# 			return mechanical_crafting()
# 		case "8" | "create:sequenced_assembly":
# 			return sequenced_assembly()
# 		case "9" | "create:emptying":
# 			print("Requires 1 item & 1 fluid in results and 1 item in ingredients.")
# 			return type1Recipe("create:filling", special="", fluid=True, chance=False)
# 		case "10" | "create:filling":
# 			print("Requires 1 item & 1 fluid in ingredients and 1 item in results.")
# 			return type1Recipe("create:filling", special="", fluid=True, chance=False)
# 		case "11" | "create:deploying":
# 			pass
# 		case _:
# 			print('Invalid Recipe Type.')
# 			return False





if __name__ == "__main__":
	"""
	Run main() until it returns true, probably not great in general, 
	but good for checking for an invalid input and asking again for this
	specific use case.
	"""

	# temp = False
	# while (not temp):
		# temp = main()

	bullets_per_gunpowder = 15
	bullets_per_casing = 5
	bullets_per_min = 15 # if amount < bullets_per_min, use amount casings, amount > bullets_per_min use, 15+(amounts/5)
	localOutput = {}

	with open('types_and_amounts.csv', newline='') as csvfile:
		types_and_amounts_with_types = csv.reader(csvfile, delimiter=',', quotechar='|')
		for x in types_and_amounts_with_types:
			print(x)
			localOutput["type"] = "create:mixing"
			localOutput["ingredients"] = [
				{
					"item": f"contenttweaker:{x[2]}_casing",
					"count": int(x[1]) if int(x[1])<=bullets_per_min else int(round(15+(int(x[1])/bullets_per_casing)))
				},
				{
					"item": "minecraft:gunpowder",
					"count": 1 if int(x[1])<=bullets_per_gunpowder else int(round(1+(int(x[1])/bullets_per_gunpowder)))
				}
			]
			localOutput["results"] = [
				{
					"item": f"craftingdead:{x[0]}",
					"count": 1
				}
			]


			with open(f"{x[0]}.json", 'w', encoding='utf-8') as f:
				json.dump(localOutput, f, ensure_ascii=False, indent=4)

	# with open(f"{input(f'[{current_item}] filename ')}.json", 'w', encoding='utf-8') as f:
	# 	json.dump(temp, f, ensure_ascii=False, indent=4)




