name_1=input("What is your name:")
name_2=input("What is your name:")
name_3=input("What is your name:")

number_of_slice=input("How many slice the pizza have:")
total_price=input("price of the pizza:")

ate_by_person_1=input(name_1+" What persentage Do you ate:")

ate_by_person_2=input(name_2+" What persentage Do you ate:")

ate_by_person_3=input(name_3+" What persentage Do you ate:")


number_of_slices_ate_by_1=float(ate_by_person_1)*float(number_of_slice)
number_of_slices_ate_by_2=float(ate_by_person_2)*float(number_of_slice)
number_of_slices_ate_by_3=float(ate_by_person_3)*float(number_of_slice)

price_paid_by_number_1=float(ate_by_person_1)*float(total_price)    
price_paid_by_number_2=float(ate_by_person_2)*float(total_price)
price_paid_by_number_3=float(ate_by_person_3)*float(total_price)

print(name_1+" ate "+str(number_of_slices_ate_by_1)+" slice and have to pay "+str(price_paid_by_number_1))

print(name_2+" ate "+str(number_of_slices_ate_by_2)+" slice and have to pay "+str(price_paid_by_number_2))

print(name_3+" ate "+str(number_of_slices_ate_by_3)+" slice and have to pay "+str(price_paid_by_number_3))

