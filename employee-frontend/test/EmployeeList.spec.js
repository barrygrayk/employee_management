import { shallowMount } from '@vue/test-utils'
import EmployeeList from '@/components/EmployeeList.vue'

describe('EmployeeList.vue', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(EmployeeList, {
      propsData: {
        employees: []
      },
      stubs: {
        'el-empty': true,
        'el-table': true,
        'el-table-column': true,
      },
      directives: {
        loading: () => {},
      },
    });
  });

  it('renders the component', () => {
    expect(wrapper.exists()).toBe(true);
  });

  it('shows the empty state when there are no employees', async () => {
    expect(wrapper.find('el-empty-stub').exists()).toBe(true);
  });

  it('does not show the table when there are no employees', async () => {
    expect(wrapper.find('el-table-stub').exists()).toBe(false);
  });

  it('returns the correct tag type', () => {
    expect(wrapper.vm.getTagType('Manager')).toBe('success');
    expect(wrapper.vm.getTagType('IN')).toBe('warning');
    expect(wrapper.vm.getTagType('JR')).toBe('');
  });
  describe('when employees list is not empty', () => {
    beforeEach(() => {
      wrapper = shallowMount(EmployeeList, {
        propsData: {
          employees: [
            { id: 1, name: 'John Doe', role: 'Manager' },
            { id: 2, name: 'Jane Doe', role: 'Employee' },
          ]
        },
        stubs: {
          'el-empty': true,
          'el-table': true,
          'el-table-column': true,
        },
        directives: {
          loading: () => {},
        },
      });
    });

    it('does not show the empty state', () => {
      expect(wrapper.find('el-empty-stub').exists()).toBe(false);
    });

    it('shows the table', () => {
      expect(wrapper.find('el-table-stub').exists()).toBe(true);
    });

    // Add more tests as needed
  });
});
