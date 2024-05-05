<template>
  <el-container>
    <el-header style="padding: 10px">
      <EmployeeHeader @searchFilter="handleSearchFilter"  @open-drawer="handleOpenDrawer" />
    </el-header>
    <el-main>
      <el-table
        :data="employees"
        style="width: 100%"
        v-loading="loading"
        @row-click="onClickEmployee"
      >
        <el-table-column type="index" width="50"> </el-table-column>
        <el-table-column prop="first_name"> </el-table-column>
        <el-table-column prop="last_name"> </el-table-column>
        <el-table-column prop="mobile_number"> </el-table-column>
      </el-table>
      <el-drawer
        :title="drawerTitle"
        :visible.sync="drawer"
        direction="ltr"
        size="45%"
      >
        <el-alert
          v-if="errorMessage"
          title="Error"
          type="error"
          :description="errorMessage"
          show-icon
        >
        </el-alert>
        <el-alert
          v-if="successMessage"
          title="success alert"
          type="success"
          :description="successMessage"
          show-icon
        ></el-alert>
        <EmployeeForm
          :errorMessage="errorMessage"
          :selectedEmployee="selectedEmployee"
          :successMessage="successMessage"
          :loading="loading"
          @submit="handleSubmitEmployee"
        />
      </el-drawer>
    </el-main>
  </el-container>
</template>

<script>
import { mapState } from 'vuex'
import { mapData } from '~/utils/dataMapper'
export default {
  name: 'IndexPage',
  data() {
    return {
      drawer: false,
      drawerTitle: '',
      selectedEmployee: null,
    }
  },
  async mounted() {
    await this.$store.dispatch('employees/fetchEmployees')
  },
  computed: {
    ...mapState({
      errorMessage: (state) => state.employees.errorMessage,
      successMessage: (state) => state.employees.successMessage,
      loading: (state) => state.employees.loading,
    }),
    employees() {
      return this.$store.getters['employees/employees']
    },
  },
  methods: {
    handleOpenDrawer() {
      this.selectedEmployee = null
      this.drawerTitle = 'New Employee'
      this.drawer = true
    },
    handleSubmitEmployee(employeeForm) {
      if (this.selectedEmployee) {
        this.$store.dispatch('employees/updateEmployee', employeeForm)
      } else {
        this.$store.dispatch('employees/createEmployee', employeeForm)
      }
    },
    onClickEmployee(row, column, event) {
      const mapToSnakeCase = false
      this.selectedEmployee = mapData(row, mapToSnakeCase)
      this.drawerTitle = 'Edit Employee'
      this.drawer = true
    },
    handleSearchFilter(searchTerm, filterTerm) {
      console.log(searchTerm, filterTerm, "index")
      this.$store.dispatch('employees/searchEmployees', {searchTerm, filterTerm})
    },
  },
}
</script>
