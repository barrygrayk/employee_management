<template>
  <el-container>
    <el-header style="padding: 10px">
      <EmployeeHeader
        @searchFilter="handleSearchFilter"
        @open-drawer="handleOpenDrawer"
      />
    </el-header>
    <el-main>
      <EmployeeList
        :employees="employees"
        :loading="loading"
        @selected-employee="handleEmployeeClick">
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
    }),
    employees() {
      return this.$store.getters['employees/employees']
    },
  },
  watch: {
    successMessage(message) {
      this.$message({
        showClose: true,
        message: message,
        type: 'success',
      })
      this.clearEmployeeForm = true
    },

    errorMessage(message) {
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
        this.$store.dispatch('employees/updateEmployee', employeeForm)
      } else {
        this.$store.dispatch('employees/createEmployee', employeeForm)
      }
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
  },
}
</script>
<style>
.el-drawer {
  background-color: #333 !important;
  color: #fff !important;
}
</style>
