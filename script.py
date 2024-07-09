def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):

  estimated_cost = 250*age - 128*sex + 370*bmi
  425*num_of_children + 24000*smoker - 12500
  
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) +  " dollars.")
  print("The estimated cost =  " + str(estimated_cost))
  return estimated_cost

maria_insurance_cost = calculate_insurance_cost("maria", 28, 0, 26.2, 3, 0)

omar_insurance_cost = calculate_insurance_cost("omar", 35,1, 22.2, 0, 1)

lisa_insurance_cost = calculate_insurance_cost("lisa", 22, 0, 27, 0, 0)
 

def diff_insurance(a,b):
  diff = a - b 

  print("The difference of insurance cost is " + str(diff))

  return diff

  def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):

    estimated_cost = 250*age - 128*sex + 370*bmi
    425*num_of_children + 24000*smoker - 12500

    return estimated_cost

  maria_insurance_cost = calculate_insurance_cost("maria", 28, 0, 26.2, 3, 0)

  omar_insurance_cost = calculate_insurance_cost("omar", 35,1, 22.2, 0, 1)

  lisa_insurance_cost = calculate_insurance_cost("lisa", 22, 0, 27, 0, 0)


diff_insurance(omar_insurance_cost, lisa_insurance_cost)

