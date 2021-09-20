# import matplotlib.pyplot as plt 
# import csv 


# x = []
# y = []
  

# with open('static/report.txt','r') as csvfile:
#     report = csv.reader(csvfile, delimiter = ',')
      
#     for row in report:
#         x.append(row[0])
#         y.append(row[1])


# plt.scatter(x, y, color = 'r', label = "x and y")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('x and y plot')
# plt.legend()
# plt.show()

x = [1,2,3,4]
b = x 
b += [30]
print(x)
print(b)
