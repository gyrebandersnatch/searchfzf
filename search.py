from youtube_search import YoutubeSearch
import os

def get_results(text, maxresults=15):
    title_tuple = {}
    results = YoutubeSearch(text, max_results=maxresults).to_dict()
    for dict in results:
        #title_tuple.append((dict['title'], dict['id']))
        title_tuple[dict['title']] = dict['id']
    return title_tuple

def convert_usable_string(title):
    return_string = ""
    for i in title:
        if return_string == "":
            return_string = i#[0]
        else:
            return_string = return_string + '\n'+ i#[0]
    return return_string
results_dict = get_results('george ezra')
list_to_find = convert_usable_string(results_dict)
stream = os.popen(f'printf "{list_to_find}"|fzf -m --reverse')
output = stream.read()
output = output.strip()
if '\n' in output:
    for i in output.splitlines():
        play=f"https://www.youtube.com/watch?v={results_dict[i.strip()]}"
        os.system(f'mpv --volume=70 --no-video --ytdl-format=best {play}')
else:
    play=f"https://www.youtube.com/watch?v={results_dict[output.strip()]}"
    os.system(f'mpv --volume=70 --no-video --ytdl-format=best {play}')