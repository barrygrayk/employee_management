<template>
  <el-form
    :model="employeeForm"
    :rules="rules"
    ref="employeeForm"
    class="employee-form"
    label-position="top"
  >
    <h5>Basic Info</h5>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-form-item label="First Name" prop="firstName">
          <el-input v-model="employeeForm.firstName"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="16">
        <el-form-item label="Last Name" prop="lastName">
          <el-input v-model="employeeForm.lastName"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <el-form-item label="Contact Number" prop="mobileNumber">
      <el-input v-model="employeeForm.mobileNumber"></el-input>
    </el-form-item>
    <el-form-item label="Email Address" prop="emailAddress">
      <el-input v-model="employeeForm.emailAddress"></el-input>
    </el-form-item>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-form-item prop="dateOfBirth" label="Date Of Birth">
          <el-date-picker
            type="date"
            placeholder="Pick a date"
            v-model="employeeForm.dateOfBirth"
            :picker-options="pickerOptions"
            style="width: 100%"
            format="yyyy-MM-dd"
          ></el-date-picker>
        </el-form-item>
      </el-col>
    </el-row>
    <h5>Address Info</h5>
    <el-form-item label="Street Address" prop="streetAddress">
      <el-input v-model="employeeForm.streetAddress"></el-input>
    </el-form-item>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-form-item label="City" prop="city">
          <el-input v-model="employeeForm.city"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="8">
        <el-form-item label="Postal Code" prop="postalCode">
          <el-input v-model="employeeForm.postalCode"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="8">
        <el-form-item label="Country" prop="country">
          <el-input v-model="employeeForm.country"></el-input>
        </el-form-item>
      </el-col>
    </el-row>
    <h5>Skills</h5>
    <el-row
      v-for="(skill, index) in employeeForm.skills"
      :key="skill.key"
      :gutter="20"
    >
      <el-col :span="8">
        <el-form-item
          label="Name"
          :prop="'skills.' + index + '.name'"
          :rules="{
            required: true,
            message: 'Name is required',
            trigger: 'blur',
          }"
        >
          <el-input v-model="skill.name"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="6">
        <el-form-item
          label="Yrs Exp"
          :prop="'skills.' + index + '.yearsOfExperience'"
          :rules="{
            required: true,
            message: 'Yrs Exp is required',
            trigger: 'blur',
          }"
        >
          <el-input v-model="skill.yearsOfExperience"></el-input>
        </el-form-item>
      </el-col>
      <el-col :span="8">
        <el-form-item
          label="Seniority"
          :prop="'skills.' + index + '.seniority'"
          :rules="{
            required: true,
            message: 'Seniority is required',
            trigger: 'blur',
          }"
        >
          <el-select v-model="skill.seniority">
            <el-option
              v-for="seniority in seniorityOptions"
              :key="seniority.value"
              :label="seniority.label"
              :value="seniority.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :span="2">
        <i
          class="el-icon-delete-solid center-icon"
          @click.prevent="removeSkill(skill)"
        ></i>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-button
          type="info"
          style="width: 100%"
          @click.prevent="addSkill()"
          icon="el-icon-plus"
          >Add New Skill</el-button
        >
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4"  class="delete-emp">
        <el-button
        type="danger"
        icon="el-icon-delete-solid"
        @click="deleteEmployeeVisible = true"
        round
          >Delete</el-button
        >
      <el-dialog
        title="Delete Employee"
        :visible.sync="deleteEmployeeVisible"
        width="20%"
        :append-to-body="true"
        center>
        <span>Are you sure you want to delete {{employeeForm.firstName }}?</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="deleteEmployeeVisible = false">Cancel</el-button>
          <el-button type="primary" @click="deleteEmployee()">Confirm</el-button>
        </span>
      </el-dialog>
      </el-col>
      <el-col :span="20" class="align-right">
        <el-button
          class="purple-button"
          v-loading="loading"
          type="primary"
          round
          icon="el-icon-plus"
          @click="onSubmitEmployee('employeeForm')"
          >Save and Add Employee</el-button
        >
      </el-col>
    </el-row>
  </el-form>
</template>

<script>
export default {
  name: 'EmployeeForm',
  data() {
    return {
      drawer: false,
      deleteEmployeeVisible: false,
      drawerTitle: 'New Employee',
      pickerOptions: {
        disabledDate(time) {
          const eighteenYearsAgo = new Date()
          eighteenYearsAgo.setFullYear(eighteenYearsAgo.getFullYear() - 1)
          return time.getTime() > eighteenYearsAgo.getTime()
        },
      },
      seniorityOptions: [
        {
          value: 'JR',
          label: 'Junior',
        },
        {
          value: 'IN',
          label: 'Intermediate',
        },
        {
          value: 'SR',
          label: 'Senior',
        },
      ],
      employeeForm: {
        id: '',
        firstName: '',
        lastName: '',
        dateOfBirth: '',
        emailAddress: '',
        mobileNumber: '',
        streetAddress: '',
        city: '',
        postalCode: '',
        country: '',
        skills: [
          {
            name: '',
            yearsOfExperience: '',
            seniority: '',
          },
        ],
      },
      rules: {
        firstName: [
          {
            required: true,
            message: 'Please enter your first name',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please enter your last name',
            trigger: 'blur',
          },
        ],
        mobileNumber: [
          {
            required: true,
            message: 'Please enter your contact number',
            trigger: 'blur',
          },
        ],
        dateOfBirth: [
          {
            type: 'date',
            required: true,
            message: 'Please pick a date of birth',
            trigger: 'blur',
          },
        ],
        emailAddress: [
          {
            required: true,
            message: 'Please input email address',
            trigger: 'blur',
          },
          {
            type: 'email',
            message: 'Please input correct email address',
            trigger: 'blur',
          },
        ],
        streetAddress: [
          {
            required: true,
            message: 'Please enter your street address',
            trigger: 'blur',
          },
        ],
        city: [
          {
            required: true,
            message: 'Please enter city',
            trigger: 'blur',
          },
        ],
        postalCode: [
          {
            required: true,
            message: 'Please enter your postal code',
            trigger: 'blur',
          },
        ],
        country: [
          {
            required: true,
            message: 'Please enter your country',
            trigger: 'blur',
          },
        ],
        lastName: [
          {
            required: true,
            message: 'Please enter your first last name',
            trigger: 'blur',
          },
        ],
      },
    }
  },
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    clearEmployeeForm: {
      type: Boolean,
      default: false,
    },
    errorMessage: {
      type: String,
      default: null,
    },
    successMessage: {
      type: String,
      default: null,
    },
    selectedEmployee: {
      type: Object,
      default: null,
    },
  },
  async mounted() {
    if (this.selectedEmployee) {
      this.employeeForm = this.selectedEmployee
      this.employeeForm.dateOfBirth = new Date(
        this.selectedEmployee.dateOfBirth
      )
    }
  },

  watch: {
    selectedEmployee: {
      immediate: true,
      handler(employee) {
        if (employee) {
          this.employeeForm = { ...employee }
          this.employeeForm.dateOfBirth = new Date(employee.dateOfBirth)
        } else {
          this.employeeForm = {
            id: '',
            firstName: '',
            lastName: '',
            dateOfBirth: '',
            emailAddress: '',
            mobileNumber: '',
            streetAddress: '',
            city: '',
            postalCode: '',
            country: '',
            skills: [
              {
                name: '',
                yearsOfExperience: '',
                seniority: '',
              },
            ],
          }
        }
      },
    },
    clearEmployeeForm(clearForm) {
      if (clearForm) {
        this.resetForm()
      }
    },
  },
  methods: {
    removeSkill(item) {
      var index = this.employeeForm.skills.indexOf(item)
      if (index !== -1) {
        this.employeeForm.skills.splice(index, 1)
      }
    },
    addSkill() {
      this.employeeForm.skills.push({
        name: '',
        yearsOfExperience: '',
        seniority: '',
      })
    },
    deleteEmployee() {
      this.$emit('deleteEmployee', this.employeeForm)
      this.deleteEmployeeVisible = false
    },
    onSubmitEmployee() {
      this.$refs.employeeForm.validate((valid) => {
        if (valid) {
          this.$emit('submit', this.employeeForm)
        }
      })
    },
    resetForm() {
      this.$refs.employeeForm.resetFields()
    },
  },
}
</script>

<style scoped>
.left-align {
  float: left;
}
.employee-form {
  padding: 20px;
}
.center-icon {
  padding-top: 60px;
}
.align-right {
  display: flex;
  justify-content: flex-end;
  padding-top: 20px;
}
.purple-button {
  background-color: #7030a0;
  border-color: #7030a0;
}
.purple-button:hover {
  background-color: #5b2480;
  border-color: #5b2480;
}
.delete-emp {
  padding-top: 20px;
}
</style>
