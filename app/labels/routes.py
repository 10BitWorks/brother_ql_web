from flask import render_template, request, current_app
from . import bp
from app import FONTS
from brother_ql.devicedependent import label_type_specs, label_sizes, ROUND_DIE_CUT_LABEL

LABEL_SIZES = [(
    name,
    label_type_specs[name]['name'],
    (label_type_specs[name]['kind'] in (
        ROUND_DIE_CUT_LABEL,))
) for name in label_sizes]

@bp.route('/project', methods=['GET', 'POST'])
def project_label():
    return render_template(
        'project_label.html', 
        font_family_names=FONTS.fontlist(), 
        label_sizes=LABEL_SIZES, 
        default_font_size=100, 
        default_label_size='62', 
        default_orientation='standard'
    )

@bp.route('/asset', methods=['GET', 'POST'])
def asset_label():
    return render_template(
        'asset_label.html', 
        font_family_names=FONTS.fontlist(), 
        label_sizes=LABEL_SIZES, 
        default_font_size=140, 
        default_label_size='62', 
        default_orientation='rotated'
    )
