from tabula import read_pdf
import pandas as pd
import requests


def get_profs_and_courses(term):
    url = 'https://registrar.nu.edu.kz/registrar_downloads/json?method=printDocument&name=school_schedule_by_term&termid=642&academiclevel=1'
    url2 = 'https://registrar.nu.edu.kz/registrar_downloads/json?method=printDocument&name=school_schedule_by_term&termid=603&academiclevel=1'
    if term == 1:
        r = requests.get(url, allow_redirects=True)
    elif term == 0:
        r = requests.get(url2, allow_redirects=True)
    open('./rating/school_schedule_by_term.pdf', 'wb').write(r.content)
    pdf = "./rating/school_schedule_by_term.pdf"
    data_format = "columns"

    dfs = read_pdf(pdf, pages='all', lattice=True, pandas_options={'header': None})
    dfs = pd.concat(dfs, ignore_index=True).replace(r'\r', r' ', regex=True)
    dfs.to_json(orient=data_format, index=(data_format == "columns"))

    dfs_new = dfs[dfs[11].notnull()]
    profs = list(set(dfs_new[11].tolist()))
    new_profs = []
    for i,prof in enumerate(profs):
        tmp = prof.split(", ")
        if type(tmp) == type([]):
            new_profs += tmp
        else:
            new_profs.append(tmp)
    new_profs = list(set(new_profs))

    prof_dict = {}
    for prof in new_profs:
        if prof == "TBA TBA" or prof == "Faculty":
            continue
        prof_dict[prof] = dfs_new[dfs_new[11].str.contains(prof)==True][0].tolist()
        #print(dfs_new.loc[dfs_new[11].isin(prof)][0].tolist())
    return prof_dict
