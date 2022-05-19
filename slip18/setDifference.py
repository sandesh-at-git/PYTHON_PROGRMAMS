# Q1. Write a program to create set difference and a symmetric difference.
set_A = {10,20,30,40,50}
set_B = {50,20,44,40,10}

print("Difference 1:",set_A.difference(set_B));
print("Difference 2:",set_B.difference(set_A));

print("Symmetric Difference:", set_A.symmetric_difference(set_B))
print("Symmetric Difference:", set_B.symmetric_difference(set_A))
