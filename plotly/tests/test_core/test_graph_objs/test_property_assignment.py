from unittest import TestCase
import plotly.graph_objs as go
from plotly.tests.test_optional.optional_utils import NumpyTestUtilsMixin


class TestAssignmentPrimitive(NumpyTestUtilsMixin, TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter(name='scatter A')

        # Assert initial state
        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'name': 'scatter A'})

        # Construct expected results
        self.expected_toplevel = {
            'type': 'scatter',
            'name': 'scatter A',
            'fillcolor': 'green'}

        self.expected_nested = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'colorbar': {'titlefont':
                                    {'family': 'courier'}}}}

    def test_toplevel_attr(self):
        assert self.scatter.fillcolor is None
        self.scatter.fillcolor = 'green'
        assert self.scatter.fillcolor == 'green'
        self.assert_fig_equal(self.scatter, self.expected_toplevel)

    def test_toplevel_item(self):
        assert self.scatter['fillcolor'] is None
        self.scatter['fillcolor'] = 'green'
        assert self.scatter['fillcolor'] == 'green'
        self.assert_fig_equal(self.scatter, self.expected_toplevel)

    def test_nested_attr(self):
        assert self.scatter.marker.colorbar.titlefont.family is None
        self.scatter.marker.colorbar.titlefont.family = 'courier'
        assert self.scatter.marker.colorbar.titlefont.family == 'courier'
        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_item(self):
        assert (self.scatter['marker']['colorbar']['titlefont']['family']
                is None)
        self.scatter['marker']['colorbar']['titlefont']['family'] = 'courier'
        assert (self.scatter['marker']['colorbar']['titlefont']['family']
                == 'courier')
        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_item_dots(self):
        assert self.scatter['marker.colorbar.titlefont.family'] is None
        self.scatter['marker.colorbar.titlefont.family'] = 'courier'
        assert self.scatter['marker.colorbar.titlefont.family'] == 'courier'
        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_item_tuple(self):
        assert self.scatter['marker.colorbar.titlefont.family'] is None
        self.scatter[('marker', 'colorbar', 'titlefont', 'family')] = 'courier'
        assert (self.scatter[('marker', 'colorbar', 'titlefont', 'family')]
                == 'courier')
        self.assert_fig_equal(self.scatter, self.expected_nested)


class TestAssignmentCompound(NumpyTestUtilsMixin, TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.scatter = go.Scatter(name='scatter A')

        # Assert initial state
        self.assert_fig_equal(self.scatter,
                              {'type': 'scatter',
                               'name': 'scatter A'})

        # Construct expected results
        self.expected_toplevel = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'color': 'yellow',
                       'size': 10}}

        self.expected_nested = {
            'type': 'scatter',
            'name': 'scatter A',
            'marker': {'colorbar': {
                'bgcolor': 'yellow',
                'thickness': 5}}}

    def test_toplevel_obj(self):
        self.assert_fig_equal(self.scatter.marker, {})
        self.scatter.marker = go.scatter.Marker(color='yellow', size=10)

        assert isinstance(self.scatter.marker, go.scatter.Marker)
        self.assert_fig_equal(self.scatter.marker,
                              self.expected_toplevel['marker'])

        self.assert_fig_equal(self.scatter, self.expected_toplevel)

    def test_toplevel_dict(self):
        self.assert_fig_equal(self.scatter['marker'], {})
        self.scatter['marker'] = dict(color='yellow', size=10)

        assert isinstance(self.scatter['marker'], go.scatter.Marker)
        self.assert_fig_equal(self.scatter.marker,
                              self.expected_toplevel['marker'])

        self.assert_fig_equal(self.scatter, self.expected_toplevel)

    def test_nested_obj(self):
        self.assert_fig_equal(self.scatter.marker.colorbar, {})
        self.scatter.marker.colorbar = go.scatter.marker.ColorBar(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter.marker.colorbar,
                          go.scatter.marker.ColorBar)
        self.assert_fig_equal(self.scatter.marker.colorbar,
                              self.expected_nested['marker']['colorbar'])

        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_dict(self):
        self.assert_fig_equal(self.scatter['marker']['colorbar'], {})
        self.scatter['marker']['colorbar'] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter['marker']['colorbar'],
                          go.scatter.marker.ColorBar)
        self.assert_fig_equal(self.scatter['marker']['colorbar'],
                              self.expected_nested['marker']['colorbar'])

        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_dict_dot(self):
        self.assert_fig_equal(self.scatter.marker.colorbar, {})
        self.scatter['marker.colorbar'] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter['marker.colorbar'],
                          go.scatter.marker.ColorBar)
        self.assert_fig_equal(self.scatter['marker.colorbar'],
                              self.expected_nested['marker']['colorbar'])

        self.assert_fig_equal(self.scatter, self.expected_nested)

    def test_nested_dict_tuple(self):
        self.assert_fig_equal(self.scatter[('marker', 'colorbar')], {})
        self.scatter[('marker', 'colorbar')] = dict(
            bgcolor='yellow', thickness=5)

        assert isinstance(self.scatter[('marker', 'colorbar')],
                          go.scatter.marker.ColorBar)
        self.assert_fig_equal(self.scatter[('marker', 'colorbar')],
                              self.expected_nested['marker']['colorbar'])

        self.assert_fig_equal(self.scatter, self.expected_nested)


class TestAssignmnetNone(NumpyTestUtilsMixin, TestCase):

    def test_toplevel(self):
        # Initialize scatter
        scatter = go.Scatter(name='scatter A',
                             y=[3, 2, 4],
                             marker={
                                 'colorbar': {'titlefont':
                                              {'family': 'courier'}}})
        expected = {
            'type': 'scatter',
            'name': 'scatter A',
            'y': [3, 2, 4],
            'marker': {'colorbar': {'titlefont':
                                    {'family': 'courier'}}}}

        self.assert_fig_equal(scatter, expected)

        # Set property not defined to None
        scatter.x = None
        self.assert_fig_equal(scatter, expected)

        scatter['line.width'] = None
        self.assert_fig_equal(scatter, expected)

        # Set defined property to None
        scatter.y = None
        expected.pop('y')
        self.assert_fig_equal(scatter, expected)

        # Set compound properties to None
        scatter[('marker', 'colorbar', 'titlefont')] = None
        expected['marker']['colorbar'].pop('titlefont')
        self.assert_fig_equal(scatter, expected)

        scatter.marker = None
        expected.pop('marker')
        self.assert_fig_equal(scatter, expected)


class TestAssignCompoundArray(NumpyTestUtilsMixin, TestCase):

    def setUp(self):
        # Construct initial scatter object
        self.parcoords = go.Parcoords(name='parcoords A')

        # Assert initial state
        self.assert_fig_equal(self.parcoords,
                              {'type': 'parcoords',
                               'name': 'parcoords A'})

        # Construct expected results
        self.expected_toplevel = {
            'type': 'parcoords',
            'name': 'parcoords A',
            'dimensions': [
                {'values': [2, 3, 1], 'visible': True},
                {'values': [1, 2, 3], 'label': 'dim1'}]}

        self.layout = go.Layout()

        self.expected_layout1 = {
            'updatemenus': [{},
                            {'font': {'family': 'courier'}}]
        }

        self.expected_layout2 = {
            'updatemenus': [{},
                            {'buttons': [
                                {}, {}, {'method': 'restyle'}]}]
        }

    def test_assign_toplevel_array(self):
        self.assertEqual(self.parcoords.dimensions, ())

        self.parcoords['dimensions'] = [
            go.parcoords.Dimension(values=[2, 3, 1], visible=True),
            dict(values=[1, 2, 3], label='dim1')]

        self.assertEqual(self.parcoords.to_plotly_json(),
                         self.expected_toplevel)

    def test_assign_nested_attr(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]
        self.assertEqual(self.layout['updatemenus'],
                         (go.layout.Updatemenu(), go.layout.Updatemenu()))

        self.layout.updatemenus[1].font.family = 'courier'
        self.assert_fig_equal(self.layout, self.expected_layout1)

    def test_assign_double_nested_attr(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout.updatemenus[1].buttons = [{}, {}, {}]

        # Assign
        self.layout.updatemenus[1].buttons[2].method = 'restyle'

        # Check
        self.assertEqual(
            self.layout.updatemenus[1].buttons[2].method,
            'restyle')
        self.assert_fig_equal(self.layout, self.expected_layout2)

    def test_assign_double_nested_item(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout['updatemenus'][1]['buttons'] = [{}, {}, {}]

        # Assign
        self.layout['updatemenus'][1]['buttons'][2]['method'] = 'restyle'

        # Check
        self.assertEqual(
            self.layout['updatemenus'][1]['buttons'][2]['method'],
            'restyle')

        self.assert_fig_equal(self.layout, self.expected_layout2)

    def test_assign_double_nested_tuple(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout.updatemenus = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout[('updatemenus', 1, 'buttons')] = [{}, {}, {}]

        # Assign
        self.layout[('updatemenus', 1, 'buttons', 2, 'method')] = 'restyle'

        # Check
        self.assertEqual(
            self.layout[('updatemenus', 1, 'buttons', 2, 'method')],
            'restyle')

        self.assert_fig_equal(self.layout, self.expected_layout2)

    def test_assign_double_nested_dot(self):
        self.assertEqual(self.layout.updatemenus, ())

        # Initialize empty updatemenus
        self.layout['updatemenus'] = [{}, {}]

        # Initialize empty buttons in updatemenu[1]
        self.layout['updatemenus.1.buttons'] = [{}, {}, {}]

        # Assign
        self.layout['updatemenus[1].buttons[2].method'] = 'restyle'

        # Check
        self.assertEqual(
            self.layout['updatemenus[1].buttons[2].method'],
            'restyle')
        self.assert_fig_equal(self.layout, self.expected_layout2)


# Public interfaces of BasePlotlyTypes without a figure
# ----------------
# (This file)
#  - Test validators do something for simple, compound, array
#  - Test preset does something for lists/tuples
#  - Test non-existant attr/item
#  - Test contains \ iter
#  - Trace.type
#  - .update version of every assignment
#  - Layout.xaxis1+


# With a figure
# --------------
# Figure properties
#   - data, layout, frames as attr, item, get/assign, contains
#   - tuples/dot props
#   - .update
#
#
#
# Use mock to catch _send_*_msg calls on Figure and test figure interactions
#  to generate these messages (Do not assume ipywidgets implementation).
#
#   - _send_addTraces_msg: add_* methods
#   - _send_moveTraces_msg: set data
#   - _send_deleteTraces_msg: set data
#   - _send_restyle_msg: assign trace prop
#   - _send_relayout_msg: assign layout prop
#   - _send_update_msg: .update() and batch_update()
#   - _send_animate_msg: batch_animate()
#
# ### Test other methods ###
#   - plotly_restyle
#   - plotly_relayout
#   - plotly_update
#
# ### on_change ###
#   - Warning if no parent figure
#   - Triggered by property assignment
#   - Triggered by .update()
#   - Triggered by plotly_relayout/restyle/update
#
# ### on_click/hover/unhover/select
#


# FigureWidget tests
# ------------------
# That need front-end like input
#
#  - on_click/hover/unhover/select
#  - on_change (e.g. zoom/pan/visible/dragmode/etc.)
#  - Defaults
#  - Remove overlapping properties
#
# Drive with (maybe wrap properties in _receive_* methods)
#     _js2py_traceDeltas
#     _js2py_layoutDelta
#     _js2py_restyle
#     _js2py_relayout
#     _js2py_update
#     _js2py_pointsCallback
#
# Check for (wrap in _send_remove*)
#     _py2js_removeLayoutProps
#     _py2js_removeTraceProps
#
# Model interactions after some use-cases
#
#  1) Drag/pan/zoom -> relayout
#  2) Set autoscale = true -> delta -> remove range
#  3) Pan/zoom on_change callback called only once
#  4) Select points dispatched properly
#  5)
#
# Note: deltas can be a relevant subset of what front-end returns now.

# Selenium tests
# --------------
#  - Defaults
#  - Removal
#  - Front-end styles update
#  - Click/drag/hover/select results on callbacks being called.

