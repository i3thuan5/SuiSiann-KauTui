from django.contrib import admin

class 對齊thai仔(admin.SimpleListFilter):
    title = '有對齊無'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'tuitse'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('0', '猶未對齊'),
            ('1', '有對齊'),
            ('2', '無對齊'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == '0':
            return queryset.filter(對齊狀態__isnull=True)
        elif self.value() == '1':
            return queryset.filter(對齊狀態__exact='True')
        elif self.value() == '2':
            return queryset.exclude(對齊狀態__isnull=True).exclude(對齊狀態__exact='True')
