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
                <el-input v-model="employeeForm.firstName"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
          <el-form-item label="Contact Number" prop="lastName">
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
                  style="width: 100%"
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
                  message: 'domain can not be null',
                  trigger: 'change',
                }"
              >
                <el-input v-model="skill.name"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="6">
              <el-form-item
                label="Yrs Exp"
                :prop="'skills.' + index + '.yearsOfExperience'"
              >
                <el-input v-model="skill.yearsOfExperience"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item
                label="Seniority"
                :prop="'skills.' + index + '.seniority'"
              >
                <el-input v-model="skill.seniority"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="2">
            <el-button
              type="danger"
              @click.prevent="removeSkill(skill)"
              icon="el-icon-delete"
              circle
            ></el-button>
          </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-button
                type="primary"
                style="width: 100%"
                @click.prevent="addSkill()"
                icon="el-icon-plus"
              >Add New Skill</el-button>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="24">
              <el-button type="primary" @click="submitForm('employeeForm')"
              >Save and Add Skill</el-button
            >
            </el-col>
          </el-row>
        </el-form>
      </el-drawer>
    </el-main>
  </el-container>
</template>

<script>

export default {
  name: 'IndexPage',
  data() {
    return {
      drawer: false, // Add this line
      drawerTitle: 'New Employee',
      employeeForm: {
        firstName: '',
        lastName: '',
        dateOfBirth: '',
        emailAddress: '',
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
            message: 'Please enter your first last name',
            trigger: 'blur',
          },
        ],
        dateOfBirth: [
          {
            type: 'date',
            required: true,
            message: 'Please pick a date of birth',
            trigger: 'change',
          },
        ],
        streetAddress: [
          {
            type: 'email',
            required: true,
            message: 'Please enter your street address',
            trigger: 'change',
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
  async mounted() {
    await this.$store.dispatch('employees/fetchEmployees')
  },
  computed: {
    employees() {
      return this.$store.getters['employees/employees']
    },
    loading() {
      return this.$store.getters['employees/loading']
    },
  },
  methods: {
    openCustomerDrawer() {
      this.drawer = true
    },
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
  },
}
</script>
