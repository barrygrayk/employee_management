<template>
  <el-container>
    <el-header style="padding: 10px">
      <EmployeeHeader
        :employeeCountText="employeeCountText()"
        @searchFilter="handleSearchFilter"
        @open-drawer="handleOpenDrawer"
      />
    </el-header>
    <el-main>
      <EmployeeList
        style="margin-top: 30px"
        :employees="employees"
        :loading="loading"
        @selected-employee="handleEmployeeClick"
      >
      </EmployeeList>
      <el-drawer
        ref="drawerContent"
        :title="drawerTitle"
        :visible.sync="drawer"
        :before-close="handleClose"
        direction="ltr"
        size="40%"
      >
        <EmployeeForm
          :errorMessage="errorMessage"
          :selectedEmployee="selectedEmployee"
          :successMessage="successMessage"
          :clearEmployeeForm="clearEmployeeForm"
          :loading="loading"
          @submit="handleSubmitEmployee"
          @deleteEmployee="handleDeleteEmployee"
        />
      </el-drawer>
    </el-main>
  </el-container>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'IndexPage',
  data() {
    return {
      drawer: false,
      drawerTitle: '',
      selectedEmployee: null,
      clearEmployeeForm: false,
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
      employees: (state) => state.employees.employees,
    }),
  },
  watch: {
    successMessage(message) {
      this.clearEmployeeForm = true
      if (!message) return
      this.$message({
        showClose: true,
        message: message,
        type: 'success',
      })
    },

    errorMessage(message) {
      if (!message) return
      this.$message.error(message)
    },
  },
  methods: {
    handleOpenDrawer() {
      this.clearEmployeeForm = false
      this.selectedEmployee = null
      this.drawerTitle = 'New Employee'
      this.drawer = true
    },
    handleSubmitEmployee(employeeForm) {
      if (this.selectedEmployee) {
        this.clearEmployeeForm = false
        this.$store.dispatch('employees/updateEmployee', employeeForm)
      } else {
        this.clearEmployeeForm = true
        this.$store.dispatch('employees/createEmployee', employeeForm)
      }
    },
    handleDeleteEmployee() {
      this.$store.dispatch('employees/deleteEmployee', this.selectedEmployee)
      this.clearEmployeeForm = true
      this.drawer = false
    },
    handleClose(done) {
      this.drawer = false
      this.clearEmployeeForm = true
      done()
    },
    handleEmployeeClick(selectedEmployee) {
      this.selectedEmployee = selectedEmployee
      this.drawerTitle = 'Edit Employee'
      this.drawer = true
    },
    handleSearchFilter(searchTerm, filterTerm) {
      this.$store.dispatch('employees/searchEmployees', {
        searchTerm,
        filterTerm,
      })
    },
    employeeCountText() {
      return this.employees.length === 1
        ? `There is ${this.employees.length} Employee`
        : this.employees.length > 1
        ? `There are ${this.employees.length} Employees`
        : `No Employees`
    },
  },
}
</script>
<style>
.el-drawer {
  background-color: #333 !important;
  color: #fff !important;
}
</style>
