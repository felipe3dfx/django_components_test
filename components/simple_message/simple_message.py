from django_components import component


@component.register('simple_message')
class SimpleMessage(component.Component):
    """A component that displays a message with optional icon."""

    template_file = 'simple_message.html'

    def get_context_data(self, style, **extras):
        """Set context data for rendering the component.

        Args:
            style (str): The style type ('warning' or 'error').
            **extras: Additional keyword arguments.
                text (str): The message text to display.
                extra_class (str): Additional CSS classes to apply.

        """
        color_style = {
            'warning': 'border-yellow-500 bg-yellow-100',
            'error': 'border-primary-500 bg-primary-100',
        }[style]

        return {
            'text': extras.get('text', ''),
            'final_class': f'{color_style} {extras.get("extra_class", "")}',
        }
