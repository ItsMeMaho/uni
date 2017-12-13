from cort.core import corpora
from cort.analysis import error_extractors
from cort.analysis import spanning_tree_algorithms
from cort.analysis import plotting
from collections import Counter
import pprint

reference = corpora.Corpus.from_file(
    "reference", open("wsj_gold_for_cort.conll")
    )

pair = corpora.Corpus.from_file("pair", open("wsj_predicted.conll"))
pair.read_antecedents(open('wsj_predicted.antecedents'))

extractor = error_extractors.ErrorExtractor(
    reference,
    spanning_tree_algorithms.recall_accessibility,
    spanning_tree_algorithms.precision_system_output
)

extractor.add_system(pair)
errors = extractor.get_errors()

pron_anaphor_errors = errors.filter(
    lambda error: error[0].attributes['type'] == "PRO" and
    error[1].attributes['type'] == "NAM"
)

errors_by_type = errors.categorize(
    lambda error: error[0].attributes['type']
)

# errors_by_type.visualize("pair")
# common noun errors
nom_rec_errs = errors_by_type["pair"]["recall_errors"]["all"]['NOM']
all_heads = [
    " ".join(err[0].attributes["head"]).lower() for err in nom_rec_errs]
most_common = Counter(all_heads).most_common(100)
with open('head_statistics_for_common_noun_errors_errors.txt', 'w') as f:
    pprint.pprint(most_common, stream=f)
# proper name
nam_rec_errs = errors_by_type["pair"]["recall_errors"]["all"]['NAM']
all_heads = [
    " ".join(err[0].attributes["head"]).lower() for err in nam_rec_errs]
most_common = Counter(all_heads).most_common(100)
with open('head_statistics_for_proper_name_errors_errors.txt', 'w') as f:
    pprint.pprint(most_common, stream=f)
# pronoun
pro_rec_errs = errors_by_type["pair"]["recall_errors"]["all"]['PRO']
all_heads = [
    " ".join(err[0].attributes["head"]).lower() for err in pro_rec_errs]
most_common = Counter(all_heads).most_common(100)
with open('head_statistics_for_pronoun_errors_errors.txt', 'w') as f:
    pprint.pprint(most_common, stream=f)
# demonstrative pronoun
dem_rec_errs = errors_by_type["pair"]["recall_errors"]["all"]['DEM']
all_heads = [
    " ".join(err[0].attributes["head"]).lower() for err in dem_rec_errs]
most_common = Counter(all_heads).most_common(100)
with open(
    'head_statistics_for_demonstrative_pronoun_errors_errors.txt', 'w'
        ) as f:
    pprint.pprint(most_common, stream=f)
# verb
vrb_rec_errs = errors_by_type["pair"]["recall_errors"]["all"]['VRB']
all_heads = [
    " ".join(err[0].attributes["head"]).lower() for err in vrb_rec_errs]
most_common = Counter(all_heads).most_common(100)
with open('head_statistics_for_verb_errors_errors.txt', 'w') as f:
    pprint.pprint(most_common, stream=f)


pair_errs = errors_by_type["pair"]["recall_errors"]["all"]
plotting.plot(
    [("pair_recall", [(cat, len(errs)) for cat, errs in pair_errs.items()])],
    "Recall Errors",
    "Type of anaphor",
    "Number of Errors")
plotting.pyplot.savefig('all_error_recall.png')

pair_prec = errors_by_type["pair"]["precision_errors"]["all"]
plotting.plot(
    [("pair_precision",
        [(cat, len(errs)) for cat, errs in pair_prec.items()])],
    "Precision Errors",
    "Type of anaphor",
    "Number of Errors")
plotting.pyplot.savefig('all_error_precision.png')

all_gold = set()
for doc in reference:
    for mention in doc.annotated_mentions:
        all_gold.add(mention)


def is_anaphor_gold(mention):
    if mention in all_gold:
        return "is_gold"
    else:
        return "is_not_gold"


is_ana_gold = errors_by_type.categorize(
    lambda err: is_anaphor_gold(err[0]))["pair"]["recall_errors"]["all"]
plotting.plot(
    [("Status of Anaphor",
        [(cat, len(errs)) for cat, errs in is_ana_gold.items()])],
    "Recall Errors",
    "Type of anaphor",
    "Number of Errors")
plotting.pyplot.savefig('anaphor_status_recall.png')
