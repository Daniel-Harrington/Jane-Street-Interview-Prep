'''

Daniel Harrington 2023

Unit conversion

The answer shown in the Jane Street SWE mock interview seemed overly complicated,
here is my attempt at a simpler solution. This solution doesn't require reconstructing
two directed graphs, and instead just uses a dictionary to store the conversion ratios.

Given the fact that the question posed facts as variable, I think avoiding constructing
2 graphs is ideal.


Original Sol:
https://www.youtube.com/watch?v=V8DGdPkBBxg&ab_channel=JaneStreet

Example Facts:

m = 3.28ft
ft = 12in
hr = 60min
min = 60sec

format = (str,float,str)

Example Queries:

2m = ? in -> Answer: 78.74
13in = ? m -> Answer: 0.33
13 in - ? hr -> "Not Convertible!"

format = (float,str,str)


'''

facts =  (("m",3.281,"ft"),("ft",12,"in"),("hr",60,"min"),("min",60,"sec"))

def parse_facts(facts):
    fact_dict = {}
    for fact in facts:
        fact_dict.update({fact[0]:(fact[1],fact[2])}) 
    return fact_dict


def convert_unit(facts,query):
    fact_dict = parse_facts(facts)

    
    amount,unit1,unit2 = query
    ratio_path = []
    unit = unit1

    # Find a path from unit1 to unit2
    while (unit in fact_dict.keys() or 
       any(unit == value[1] for value in fact_dict.values())) and unit != unit2:
        
        if unit in fact_dict.keys():
            ratio_path.append(fact_dict[unit][0])
            unit = fact_dict[unit][1]
        else:
            for key,value in fact_dict.items():
                if unit == value[1]:
                    ratio_path.append(1/fact_dict[key][0])
                    unit = key
            del fact_dict[unit]
    if unit != unit2:
        return "Not Convertible!"
    else:
        for ratio in ratio_path:
            amount = amount * ratio
        return amount
    

print(convert_unit(facts,(60,"in","m")))
print(convert_unit(facts,(1,"m","m")))
print(convert_unit(facts,(60,"sec","m")))
print(convert_unit(facts,(4,"hr","min")))
print(convert_unit(facts,(60,"ft","m")))