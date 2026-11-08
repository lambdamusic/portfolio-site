from django.conf import settings


def site_url(request):
    """Expose SITE_URL to templates, e.g. for the canonical link."""
    return {'SITE_URL': settings.SITE_URL}


def layout_proto(request):
    """The layout prototype in use, if any (see portfolioapp/proto.py)."""
    from .proto import (current_layout, current_post_layout, current_project_layout,
                        LAYOUTS, POST_LAYOUTS, PROJECT_LAYOUTS)
    return {'layout': current_layout(request), 'proto_layouts': LAYOUTS.items(),
            'post_layout': current_post_layout(request), 'proto_posts': POST_LAYOUTS.items(),
            'project_layout': current_project_layout(request),
            'proto_projects': PROJECT_LAYOUTS.items()}
