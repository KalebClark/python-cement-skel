from cement.core.controller import CementBaseController, expose


class __CONTROLLER_NAME__(CementBaseController):
    class Meta:
        label = '__CONTROLLER_LABEL__'
        aliases = ['__CONTROLLER_ALIAS__']
        description = ''
        stacked_on = '__STACKED_ON__'
        stacked_type = '__STACKED_TYPE__'

    @expose(help='woot')
    def example(self):
        print 'Entering: __CONTROLLER_NAME__.example()'