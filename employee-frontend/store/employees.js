import { mapData } from '~/utils/dataMapper';

export const state = () => ({
  employees: [],
  loading: false,
  createErrorMessage: null,
  createSuccessMessage: null,
});

export const mutations = {
  SET_LOADING(state, value) {
    state.loading = value;
  },
  SET_EMPLOYEES(state, employees) {
    state.employees = employees;
  },
  CREATE_EMPLOYEE(state, employee) {
    state.employees.push(employee);
    state.createSuccessMessage = 'Employee created successfully.'
    state.createErrorMessage = null;
  },
  CREATE_ERROR(state, message) {
    state.createErrorMessage = message;
    state.createSuccessMessage = null
  },
  UPDATE_EMPLOYEE(state, employee) {
    const itemIndex = state.employees.findIndex((employee) => employee.id === updatedItem.id);
    if (itemIndex !== -1) {
      state.employees[itemIndex] = updatedItem;
    }
  },
  DELETE_EMPLOYEE(state, employeeId) {
    state.employees = state.items.filter((item) => item.id !== itemId);
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
    let mappedEmployeeData = mapData(employeeData);
    const response = await this.$axios.post("/employees/", mappedEmployeeData)
    .then((employee) => {
      commit('CREATE_EMPLOYEE', employee.data);
    })
    .catch(error => {
      commit('CREATE_ERROR', error);
    })
    .finally(() => {
      commit('SET_LOADING', false)
    });

  },
  async updateEmployee({ commit }, employeeData) {
    let mappedEmployeeData = mapData(employeeData);
    const response = await this.$axios.put(`/employees/${itemData.id}`, mappedEmployeeData);
    commit('UPDATE_EMPLOYEE', response.data);
    commit('SET_ITEMS', response.data);
    commit('SET_LOADING', false);
  },
  async deleteEmployee({ commit }, employeeId) {
    await this.$axios.delete(`/employees/${employeeId}`);
    commit('DELETE_EMPLOYEE', employeeId);
    commit('SET_ITEMS', response.data);
    commit('SET_LOADING', false);
  },
};

export const getters = {
  employees: (state) => state.employees,
  loading: (state) => state.loading,
};
