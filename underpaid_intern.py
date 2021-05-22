def make_a_table(data):
    headline = data['headline']
    subtitle = data['subtitle']
    columns = data['columns']
    lines = data['lines']
    column_titles = data['column_titles']

    filename = headline + '.html'
    file = open(filename, 'w+')
    file.write('<HTML>\n')
    file.write('<head>')
    file.write('<headl style="font-size:29px; font-family:Arial">')
    file.write(headline)
    file.write('</headl>\n')
    file.write('<p>')
    file.write(subtitle)
    file.write('</p>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('<style type="text/css">\n'
               + '.tg  {border-collapse:collapse;border-color:#9e9e9e;border-spacing:0}\n'
               + '.tg td{background-color:#000000;border-color:#000000;border-style:solid;border-width:1px;color:#000000;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}\n'
               + '.tg th{background-color:#f0f0f0;border-color:#000000;border-style:solid;border-width:1px;color:#000000;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}\n'
               + '.tg .tg-gray{background-color:#efefef;border-color:#000000;text-align:left;vertical-align:top;}\n'
               + '.tg .tg-blue{background-color:#dae8fc;border-color:#000000;text-align:left;vertical-align:top;}\n'
               + '.tg .tg-white{background-color:#fcfcfc;border-color:#000000;text-align:left;vertical-align:top;}\n'
               + '</style>\n')
    file.write('<table class="tg"  border=1 cellspacing=0 cellpadding=0>\n')
    file.write('<thead>\n')

    file.write('\t<tr>\n')
    i = 0
    while i < int(columns):
        file.write('\t\t<th class="tg-blue">')
        file.write('\t\t' + column_titles[i])
        file.write('\t\t</th>\n')
        i = i + 1
    file.write('\t</tr>\n')
    file.write('</thead>\n')

    file.write('<tbody>\n')
    i = 0
    while i < int(lines):
        j = 0
        file.write('\t<tr>\n')
        if i % 2 == 0:
            while j < int(columns):
                file.write('\t\t<td class="tg-white">__________</td>\n')
                j = j + 1
        else:
            while j < int(columns):
                file.write('\t\t<td class="tg-gray">__________</td>\n')
                j = j + 1
        file.write('\t</tr>\n')
        i = i + 1
    file.write('</tbody\n')
    file.write('</table\n')
    file.write('</body>\n')
    file.write('</HTML>')
    file.close()
