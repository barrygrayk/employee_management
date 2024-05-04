<template>
  <el-container>
    <el-header>
      <el-row>
        <el-col :span="16">
          <h2>Employees</h2>
        </el-col>
        <el-col :span="8">
          <el-button
            type="primary"
            round
            icon="el-icon-plus"
            @click="openCustomerDrawer()"
            >Employee</el-button
          >
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <el-table :data="employees" style="width: 100%" v-loading="loading">
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
export default {
  name: 'IndexPage',
  data() {
    return {
      drawer: false, // Add this line
      drawerTitle: 'New Employee',
    }
  },
  async mounted() {
    await this.$store.dispatch('employees/fetchEmployees')
  },
  computed: {
    ...mapState({
      errorMessage: (state) => state.employees.createErrorMessage,
      successMessage: (state) => state.employees.createSuccessMessage,
      loading: (state) => state.employees.loading,
    }),
    employees() {
      return this.$store.getters['employees/employees']
    },
  },
  methods: {
    openCustomerDrawer() {
      this.drawer = true
    },
    removeSkill(item) {
      // var index = this.employeeForm.skills.indexOf(item)
      // if (index !== -1) {
      //   this.employeeForm.skills.splice(index, 1)
      // }
    },
    handleSubmitEmployee(employeeForm) {
      this.$store.dispatch('employees/createEmployee', employeeForm)
    },
  },
}
</script>
