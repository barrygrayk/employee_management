export const state = () => ({
  employees: [],
  loading: false,
});

export const mutations = {
  SET_LOADING(state, value) {
    state.loading = value;
  },
  SET_EMPLOYEES(state, employees) {
    state.employees = employees;
  },
  ADD_EMPLOYEE(state, employee) {
    state.items.push(employee);
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
    const response = await this.$axios.get("/employees");
    commit('SET_EMPLOYEES', response.data);
    commit('SET_LOADING', false);
  },
  async createEmployee({ commit }, employeeData) {
    commit('SET_LOADING', true);
    const response = await this.$axios.post("employees", employeeData);
    commit('ADD_EMPLOYEE', response.data);
    commit('SET_ITEMS', response.data);
    commit('SET_LOADING', false);
  },
  async updateEmployee({ commit }, employeeData) {
    const response = await this.$axios.put(`/employees/${itemData.id}`, employeeData);
    commit('UPDATE_EMPLOYEE', response.data);
    commit('SET_ITEMS', response.data);
    commit('SET_LOADING', false);
  },
  async deleteEmployee({ commit }, employeeId) {
    await this.$axios.delete(`employees/${employeeId}`);
    commit('DELETE_EMPLOYEE', employeeId);
    commit('SET_ITEMS', response.data);
    commit('SET_LOADING', false);
  },
};

export const getters = {
  employees: (state) => state.employees,
  loading: (state) => state.loading,
};
