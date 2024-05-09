<template>
  <el-row :gutter="20" class="center-row">
    <el-col :span="4">
      <h2>Employees</h2>
      <small>{{ employeeCountText }}</small>
    </el-col>
    <el-col :span="12">
      <el-input
        placeholder="Search"
        v-model="searchTerm"
        @input="onSearchFilterEmployee"
      >
        <i slot="prefix" class="el-input__icon el-icon-search"></i>
      </el-input>
    </el-col>
    <el-col :span="6">
      <el-select v-model="filterTerm" placeholder="Filter By" @change="onSearchFilterEmployee">
        <el-option
          v-for="item in filterOptions"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </el-col>
    <el-col :span="4" class="align-right">
      <el-button
        type="primary"
        round
        class="purple-button"
        icon="el-icon-plus"
        @click="openCustomerDrawer()"
        >New Employee</el-button
      >
    </el-col>
  </el-row>
</template>
<script>
export default {
  data() {
    return {
      searchTerm: '',
      filterTerm: '',
      filterOptions: [
        {
          label: 'Date of Birth - ASC',
          value: 'date_of_birth',
        },
        {
          label: 'Date of Birth - DESC',
          value: '-date_of_birth',
        },
        {
          label: 'Skill - ASC',
          value: 'skills__name',
        },
        {
          label: 'Skill - DESC',
          value: '-skills__name',
        },
      ],
    }
  },
  props: {
    employeeCountText: {
      type: String,
      default: 'No Employees',
    },
  },
  methods: {
    onSearchFilterEmployee() {
      this.$emit('searchFilter', this.searchTerm, this.filterTerm)
    },
    openCustomerDrawer() {
      this.$emit('open-drawer')
    },
  },
}
</script>

<style scoped>
.center-row {
  display: flex;
  align-items: center;
}
.align-right {
  display: flex;
  justify-content: flex-end;
}
.purple-button {
  background-color: #7030a0;
  border-color: #7030a0;
}
.purple-button:hover {
  background-color: #5b2480;
  border-color: #5b2480;
}
</style>
