from cort.core import corpora
from cort.analysis import error_extractors
from cort.analysis import spanning_tree_algorithms
from cort.analysis import plotting

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

pair_errs = errors_by_type["pair"]["recall_errors"]["all"]
# pairs_errs = pron_anaphor_errors['pair']['recall_errors']['all']
plotting.plot(
    [("pair_recall", [(cat, len(errs)) for cat, errs in pair_errs.items()])],
    "Recall Errors",
    "Type of anaphor",
    "Number of Errors")

pair_prec = errors_by_type["pair"]["precision_errors"]["all"]
plotting.plot(
    [("pair_precision",
        [(cat, len(errs)) for cat, errs in pair_prec.items()])],
    "Precision Errors",
    "Type of anaphor",
    "Number of Errors")

pair_dec = errors_by_type["pair"]["decisions"]["all"]
plotting.plot(
    [("pair_decisions", [(cat, len(errs)) for cat, errs in pair_dec.items()])],
    "Decisions Errors",
    "Type of anaphor",
    "Number of Errors")
