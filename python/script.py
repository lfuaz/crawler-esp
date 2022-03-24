
from google_images_search import GoogleImagesSearch
# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX

dwnl = []
def my_progressbar(url,progress):
    if url not in dwnl:
        dwnl.append(url)
        print(url)
        

gis = GoogleImagesSearch("AIzaSyClG0cWjXj33BEBuuBB8CverGjDKrbTwtY", "91dd71e72566b4d42", progressbar_fn=my_progressbar)

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value

search = input("Recherche : ")
nb = input("Combien : ")



_search_params = {
    'q': search,
    'num': int(nb),
}

# this will search, download and resize:
gis.search(search_params=_search_params, path_to_dir='dwnl/'+_search_params['q'], width=500, height=500)

