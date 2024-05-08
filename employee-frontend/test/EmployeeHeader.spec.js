import { shallowMount } from '@vue/test-utils'
import EmployeeHeader from '@/components/EmployeeHeader.vue'

describe('EmployeeHeader.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(EmployeeHeader, {
        stubs: {
          'el-button': true,
          'el-form': {
            template: '<div />',
            methods: {
              validate: (callback) => callback(true),
            },
          },
        },
    });
  });


  it('emits onSearchFilterEmployee event', () => {
    wrapper.vm.onSearchFilterEmployee();
    expect(wrapper.emitted('searchFilter')).toBeTruthy();
  });

  it('emits openCustomerDrawer event', () => {
    wrapper.vm.openCustomerDrawer();
    expect(wrapper.emitted('open-drawer')).toBeTruthy();
  });
  it('filterOptions has 4 values', () => {
    expect(wrapper.vm.filterOptions.length).toBe(4);
  });

});
