export default function createReportObject(employeesList) {
    const obj = {
      allEmployees: employeesList,
      getNumberOfDepartments() {
        const keysArray = Object.keys(this.allEmployees);
        const count = keysArray.length;
        return count;
      },
    };
    return obj;
  }
