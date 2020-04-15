# importing modules
import io
import matplotlib.pyplot as plotter

class GenerateGraphModels:
    def __init__(self, graphId):
        pass
        self.dataId = graphId
    
    def checkGraphIdentity(self):
        pass
        # checking graph conditions
        if self.dataId == "salary" or self.dataId == "Salary" or self.dataId == "SALARY":
            self.salaryStatus()
        elif self.dataId == "employee" or self.dataId == "Employee" or self.dataId == "EMPLOYEE":
            self.employeeStatus()
        else:
            print("NO SUCH DATA!")
    
    def salaryStatus(self):
        salarydata = [30, 62, 86.7]
        yearIndex = [2017, 2018, 2019]
        
        # plotting a graph
        plotter.plot(yearIndex, salarydata)
        plotter.title("Salary Index")
        plotter.xlabel("Years")
        plotter.ylabel("Salary in Crores (INR)")
        plotter.legend(["Salary Index Rate in INR"])
        plotter.show()
    
    def employeeStatus(self):
        employeeData = [1000, 760, 890]
        yearIndex = [2017, 2018, 2019]
        
        # plotting a graph
        plotter.plot(yearIndex, employeeData)
        plotter.title("Employee Recruitment Index")
        plotter.xlabel("Years")
        plotter.ylabel("Employees Recruited")
        plotter.legend(["No. of employees hired"])
        plotter.show()
        
'''main function'''
graphIndexGeneratorSalary = GenerateGraphModels("salary")
graphIndexGeneratorSalary.checkGraphIdentity()
graphIndexGeneratorEmployee = GenerateGraphModels("employee")
graphIndexGeneratorEmployee.checkGraphIdentity()
