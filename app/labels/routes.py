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
        font_family_groups=FONTS.grouped_fontlist(current_app.config['BRAND_FONT_FAMILIES']),
        default_font_family=current_app.config['LABEL_DEFAULT_FONT_FAMILY'],
        label_sizes=LABEL_SIZES,
        default_font_size=100,
        default_label_size='62',
        default_orientation='standard'
    )

@bp.route('/asset', methods=['GET', 'POST'])
def asset_label():
    return render_template(
        'asset_label.html',
        font_family_groups=FONTS.grouped_fontlist(current_app.config['BRAND_FONT_FAMILIES']),
        default_font_family=current_app.config['LABEL_DEFAULT_FONT_FAMILY'],
        label_sizes=LABEL_SIZES,
        default_font_size=140,
        default_label_size='62',
        default_orientation='rotated'
    )
