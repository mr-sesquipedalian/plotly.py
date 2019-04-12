

import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='visible', parent_name='splom.dimension', **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuessrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='valuessrc', parent_name='splom.dimension', **kwargs
    ):
        super(ValuessrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class ValuesValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(
        self, plotly_name='values', parent_name='splom.dimension', **kwargs
    ):
        super(ValuesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc+clearAxisTypes'),
            role=kwargs.pop('role', 'data'),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='templateitemname',
        parent_name='splom.dimension',
        **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='name', parent_name='splom.dimension', **kwargs
    ):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='label', parent_name='splom.dimension', **kwargs
    ):
        super(LabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )


import _plotly_utils.basevalidators


class AxisValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='axis', parent_name='splom.dimension', **kwargs
    ):
        super(AxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Axis'),
            data_docs=kwargs.pop(
                'data_docs', """
            matches
                Determines whether or not the x & y axes
                generated by this dimension match. Equivalent
                to setting the `matches` axis attribute in the
                layout with the correct axis id.
            type
                Sets the axis type for this dimension's
                generated x and y axes. Note that the axis
                `type` values set in layout take precedence
                over this attribute.
"""
            ),
            **kwargs
        )
