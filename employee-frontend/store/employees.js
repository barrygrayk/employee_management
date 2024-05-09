import { mapData } from '~/utils/dataMapper';
import { buildQueryString } from '~/utils/queryBuilder';
import moment from 'moment';

export const state = () => ({
  employees: [],
  loading: false,
  errorMessage: null,
  successMessage: null,
});

export const mutations = {
  SET_LOADING(state, value) {
    state.loading = value;
    state.errorMessage = null;
    state.successMessage = null
  },
  SET_EMPLOYEES(state, employees) {
    state.employees = employees;
    state.loading = false;
  },
  CREATE_EMPLOYEE(state, employee) {
    state.employees.push(employee);
    state.successMessage = `Employee created successfully - ${employee.employee_code}.`
    state.errorMessage = null;
    state.loading = false;
  },
  ERROR(state, message) {
    state.errorMessage = message;
    state.successMessage = null
    state.loading = false;
  },
  UPDATE_EMPLOYEE(state, employee) {
    const itemIndex = state.employees.findIndex((employee) => employee.id === employee.id);
    if (itemIndex !== -1) {
      state.employees.splice(itemIndex, 1, employee);
    }
    state.successMessage = `Employee updated successfully - ${employee.employee_code}.`
    state.errorMessage = null;
    state.loading = false;
  },
  DELETE_EMPLOYEE(state, deletedEmployee) {
    console.log(deletedEmployee, "-->");
    state.employees = state.employees.filter((employee) => employee.id !== deletedEmployee.id);
    state.successMessage = `Employee deleted successfully - ${deletedEmployee.employeeCode}.`
    state.errorMessage = null;
    state.loading = false;
  },
};

export const actions = {
  async fetchEmployees({ commit }) {
    commit('SET_LOADING', true);
    const response = await this.$axios.get("/employees/");
    commit('SET_EMPLOYEES', response.data);
    commit('SET_LOADING', false);
  },
  async createEmployee({ commit }, employeeData) {
    commit('SET_LOADING', true);
    const dateOfBirth = moment(employeeData.dateOfBirth).format('YYYY-MM-DD');
    employeeData.dateOfBirth = dateOfBirth;
    let mappedEmployeeData = mapData(employeeData);
    this.$axios.post("/employees/", mappedEmployeeData)
    .then((employee) => {
      commit('CREATE_EMPLOYEE', employee.data);
    })
    .catch(error => {
      commit('ERROR', error);
    })

  },
  async updateEmployee({ commit }, employeeData) {
    commit('SET_LOADING', true);
    const dateOfBirth = moment(employeeData.dateOfBirth).format('YYYY-MM-DD')
    employeeData.dateOfBirth = dateOfBirth;
    let mappedEmployeeData = mapData(employeeData);
    await this.$axios.put(`/employees/${employeeData.id}/`, mappedEmployeeData)
    .then((employee) => {
      commit('UPDATE_EMPLOYEE', employee.data);
    })
    .catch(error => {
      commit('ERROR', error);
    })
  },

  async searchEmployees({ commit }, terms) {
    commit('SET_LOADING', true);
    const query = buildQueryString({ search: terms.searchTerm, ordering: terms.filterTerm });
    await this.$axios.get(`/employees/?${query}`)
      .then(response => {
        commit('SET_EMPLOYEES', response.data);
        commit('SET_LOADING', false);
      })
      .catch(error => {
        commit('ERROR', error);
      });
  },
  async deleteEmployee({ commit }, employee) {
    await this.$axios.delete(`/employees/${employee.id}`)
    .then(() => {
      commit('DELETE_EMPLOYEE', employee);
    })
    .catch(error => {
      commit('ERROR', error);
    })
  },
};

export const getters = {
  employees: (state) => state.employees,
  loading: (state) => state.loading,
};
