import { shallowMount } from '@vue/test-utils';
import EmployeeForm from '@/components/EmployeeForm.vue';

describe('EmployeeForm.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(EmployeeForm, {
      propsData: {
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
      },
      stubs: {
        'el-col': true,
        'el-row': true,
        'el-button': true,
      },
      directives: {
        loading: () => {},
      },
    });
  });

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('emits "submit" event with form data when form is submitted', async () => {
    wrapper.vm.employeeForm.firstName = 'John';
    wrapper.vm.employeeForm.lastName = 'Doe';
    wrapper.vm.employeeForm.dateOfBirth = '1995-06-16';
    wrapper.vm.employeeForm.emailAddress = 'barry@gmail.com';
    wrapper.vm.employeeForm.streetAddress = '1 Mumbai Street';
    wrapper.vm.employeeForm.postalCode = '1101';
    wrapper.vm.employeeForm.city = 'Kitwe';
    wrapper.vm.employeeForm.country = 'Zambia';
    wrapper.vm.employeeForm.skills = [
      {
        name: 'Vue.js',
        yearsOfExperience: '2',
        seniority: 'JR',
      },
    ]
    await wrapper.vm.onSubmitEmployee();
    expect(wrapper.emitted().submit).toBeTruthy();
  });
  it('has all the required fields', () => {
    const fields = ['firstName', 'lastName', 'dateOfBirth', 'emailAddress', 'streetAddress', 'city', 'postalCode', 'country', 'skills'];
    fields.forEach(field => {
      expect(wrapper.vm.employeeForm).toHaveProperty(field);
    });
  });
  it('adds a new skill when addSkill is called', () => {
    const initialLength = wrapper.vm.employeeForm.skills.length;
    wrapper.vm.addSkill();
    expect(wrapper.vm.employeeForm.skills.length).toBe(initialLength + 1);
  });
  it('removes a skill when removeSkill is called', () => {
    const skill = {
      name: 'JavaScript',
      yearsOfExperience: '5',
      seniority: 'Senior',
    };
    wrapper.vm.employeeForm.skills.push(skill);
    wrapper.vm.removeSkill(skill);
    // Check if the skill was removed from the array
    expect(wrapper.vm.employeeForm.skills).not.toContain(skill);
  });
});
