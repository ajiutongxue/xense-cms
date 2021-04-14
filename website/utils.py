def x_get_page_tmpl(default_tmpl, category, page):
    """
    获取详情页面使用的模版文件名
    """
    tmpl = default_tmpl
    if category.default_article_self_template != 'DONT-USE':
        tmpl = category.default_article_self_template
    if category.article_self_template and category.article_self_template.strip():
        tmpl = category.article_self_template
    if page.custom_tmpl and page.custom_tmpl.strip():
        tmpl = page.custom_tmpl
    return tmpl


def x_get_list_tmpl(default_tmpl, category):
    """
    获取列表页面使用的模版文件名
    """
    tmpl = default_tmpl
    if category.default_self_template != 'DONT-USE':
        tmpl = category.default_self_template
    if category.self_template and category.self_template.strip():
        tmpl = category.self_template
    return tmpl
