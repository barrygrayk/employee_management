<template>
  <div>
    <el-table
      v-if="employees.length"
      :data="employees"
      style="width: 100%"
      v-loading="loading"
      @row-click="onClickEmployee"
    >
      <el-table-column label="No." type="index" width="50"> </el-table-column>
      <el-table-column label="First Name" prop="first_name"> </el-table-column>
      <el-table-column label="Last Name" prop="last_name"> </el-table-column>
      <el-table-column label="Mobile Number" prop="mobile_number">
      </el-table-column>
      <el-table-column label="Date of Birth" prop="date_of_birth">
      </el-table-column>
      <el-table-column label="Skills">
        <template slot-scope="scope">
          <div class="skills-container">
            <el-tag
              :type="getTagType(skill.seniority)"
              size="small"
              v-for="(skill, index) in scope.row.skills"
              :key="index"
            >
              {{ skill.name }}
            </el-tag>
          </div>
        </template>
      </el-table-column>
    </el-table>
    <el-empty
      v-if="!employees.length"
      image="/logo.png"
      :image-size=400
      description="There is nothing here"
    >
      <p>
        Create a new employee by clicking the New Employee button to get started
      </p>
    </el-empty>
  </div>
</template>

<script>
import { mapData } from '~/utils/dataMapper'
export default {
  name: 'EmployeeList',
  data() {
    return {
      drawer: false,
      drawerTitle: '',
      selectedEmployee: null,
      clearEmployeeForm: false,
    }
  },
  props: {
    employees: {
      type: Array,
      default: () => [],
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    onClickEmployee(employee, column, event) {
      const mapToSnakeCase = false
      this.selectedEmployee = mapData(employee, mapToSnakeCase)
      this.$emit('selected-employee', this.selectedEmployee)
    },
    getTagType(seniority) {
      switch (seniority) {
        case 'JR':
          return ''
        case 'IN':
          return 'warning'
        default:
          return 'success'
      }
    },
  },
}
</script>
<style>
.el-table th {
  background-color: #222933 !important;
  color: #fff !important;
}
.skills-container {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
}
</style>
