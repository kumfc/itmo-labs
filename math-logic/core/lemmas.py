main_lemma = ["{var}",
              "({var} -> (!{var} -> {var}))",
              "(!{var} -> {var})",
              "(!{var} -> (!{var} -> !{var}))",
              "((!{var} -> (!{var} -> !{var})) -> ((!{var} -> ((!{var} -> !{var}) -> !{var})) -> (!{var} -> !{var})))",
              "((!{var} -> ((!{var} -> !{var}) -> !{var})) -> (!{var} -> !{var}))",
              "(!{var} -> ((!{var} -> !{var}) -> !{var}))",
              "(!{var} -> !{var})",
              "((!{var} -> {var}) -> ((!{var} -> !{var}) -> !!{var}))",
              "((!{var} -> !{var}) -> !!{var})",
              "!!{var}"]


def get_main_proof(var):
    r = []
    for line in main_lemma:
        r.append(line.format(var=var))
    return r


axiom10_lemma = ["({var} -> (!!{var} -> {var}))",
                 "(({var} -> (!!{var} -> {var})) -> (!(!!{var} -> {var}) -> ({var} -> (!!{var} -> {var}))))",
                 "(!(!!{var} -> {var}) -> ({var} -> (!!{var} -> {var})))",
                 "(!(!!{var} -> {var}) -> ({var} -> !(!!{var} -> {var})))",
                 "(!(!!{var} -> {var}) -> (!(!!{var} -> {var}) -> !(!!{var} -> {var})))",
                 "(!(!!{var} -> {var}) -> ((!(!!{var} -> {var}) -> !(!!{var} -> {var})) -> !(!!{var} -> {var})))",
                 "((!(!!{var} -> {var}) -> (!(!!{var} -> {var}) -> !(!!{var} -> {var}))) -> ((!(!!{var} -> {var}) -> ((!(!!{var} -> {var}) -> !(!!{var} -> {var})) -> !(!!{var} -> {var}))) -> (!(!!{var} -> {var}) -> !(!!{var} -> {var}))))",
                 "((!(!!{var} -> {var}) -> ((!(!!{var} -> {var}) -> !(!!{var} -> {var})) -> !(!!{var} -> {var}))) -> (!(!!{var} -> {var}) -> !(!!{var} -> {var})))",
                 "(!(!!{var} -> {var}) -> !(!!{var} -> {var}))",
                 "(({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var}))",
                 "((({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var})) -> (!(!!{var} -> {var}) -> (({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var}))))",
                 "(!(!!{var} -> {var}) -> (({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var})))",
                 "((!(!!{var} -> {var}) -> ({var} -> (!!{var} -> {var}))) -> ((!(!!{var} -> {var}) -> (({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var}))) -> (!(!!{var} -> {var}) -> (({var} -> !(!!{var} -> {var})) -> !{var}))))",
                 "((!(!!{var} -> {var}) -> (({var} -> (!!{var} -> {var})) -> (({var} -> !(!!{var} -> {var})) -> !{var}))) -> (!(!!{var} -> {var}) -> (({var} -> !(!!{var} -> {var})) -> !{var})))",
                 "(!(!!{var} -> {var}) -> (({var} -> !(!!{var} -> {var})) -> !{var}))",
                 "((!(!!{var} -> {var}) -> ({var} -> !(!!{var} -> {var}))) -> ((!(!!{var} -> {var}) -> (({var} -> !(!!{var} -> {var})) -> !{var})) -> (!(!!{var} -> {var}) -> !{var})))",
                 "((!(!!{var} -> {var}) -> (({var} -> !(!!{var} -> {var})) -> !{var})) -> (!(!!{var} -> {var}) -> !{var}))",
                 "(!(!!{var} -> {var}) -> !{var})",
                 "(!{var} -> (!!{var} -> {var}))",
                 "((!{var} -> (!!{var} -> {var})) -> (!(!!{var} -> {var}) -> (!{var} -> (!!{var} -> {var}))))",
                 "(!(!!{var} -> {var}) -> (!{var} -> (!!{var} -> {var})))",
                 "((!(!!{var} -> {var}) -> !{var}) -> ((!(!!{var} -> {var}) -> (!{var} -> (!!{var} -> {var}))) -> (!(!!{var} -> {var}) -> (!!{var} -> {var}))))",
                 "((!(!!{var} -> {var}) -> (!{var} -> (!!{var} -> {var}))) -> (!(!!{var} -> {var}) -> (!!{var} -> {var})))",
                 "(!(!!{var} -> {var}) -> (!!{var} -> {var}))",
                 "((!(!!{var} -> {var}) -> (!!{var} -> {var})) -> ((!(!!{var} -> {var}) -> !(!!{var} -> {var})) -> !!(!!{var} -> {var})))",
                 "((!(!!{var} -> {var}) -> !(!!{var} -> {var})) -> !!(!!{var} -> {var}))",
                 "!!(!!{var} -> {var})"]


def get_axiom10_proof(var):
    r = []
    for line in axiom10_lemma:
        r.append(line.format(var=var))
    return r


modus_ponens_lemma = ["(!{var2} -> (({var1} -> {var2}) -> !{var2}))",
                      "(!{var2} -> ({var1} -> !{var2}))",
                      "((!{var2} -> ({var1} -> !{var2})) -> (!{var2} -> (!{var2} -> ({var1} -> !{var2}))))",
                      "(!{var2} -> (!{var2} -> ({var1} -> !{var2})))",
                      "((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))",
                      "(((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2})))) -> (!{var2} -> ((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))))",
                      "(!{var2} -> ((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2})))))",
                      "((!{var2} -> (!{var2} -> ({var1} -> !{var2}))) -> ((!{var2} -> ((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))) -> (!{var2} -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))))",
                      "((!{var2} -> ((!{var2} -> ({var1} -> !{var2})) -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))) -> (!{var2} -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2})))))",
                      "(!{var2} -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))))",
                      "((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))",
                      "(((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2})))) -> (!{var2} -> ((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2})))))",
                      "((!{var2} -> (({var1} -> {var2}) -> !{var2})) -> ((!{var2} -> ((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> !{var2}) -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2})))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))",
                      "((!{var2} -> (({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2})))) -> ((!{var2} -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2})))) -> (!{var2} -> (({var1} -> {var2}) -> ({var1} -> !{var2})))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> (!{var2} -> ({var1} -> !{var2}))) -> (({var1} -> {var2}) -> ({var1} -> !{var2})))) -> (!{var2} -> (({var1} -> {var2}) -> ({var1} -> !{var2}))))",
                      "(!{var2} -> (({var1} -> {var2}) -> ({var1} -> !{var2})))",
                      "(({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1}))",
                      "((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (!{var2} -> (({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1}))))",
                      "(!{var2} -> (({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})))",
                      "((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))",
                      "(((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1}))) -> (!{var2} -> ((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1}))))",
                      "((!{var2} -> (({var1} -> {var2}) -> ({var1} -> !{var2}))) -> ((!{var2} -> ((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))) -> (!{var2} -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> ({var1} -> !{var2})) -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))) -> (!{var2} -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1}))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1})))",
                      "((!{var2} -> (({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1}))) -> ((!{var2} -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1}))) -> (!{var2} -> (({var1} -> {var2}) -> !{var1}))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> (({var1} -> !{var2}) -> !{var1})) -> (({var1} -> {var2}) -> !{var1}))) -> (!{var2} -> (({var1} -> {var2}) -> !{var1})))",
                      "(!{var2} -> (({var1} -> {var2}) -> !{var1}))",
                      "!!{var1}",
                      "(!!{var1} -> (!{var2} -> !!{var1}))",
                      "(!{var2} -> !!{var1})",
                      "(!!{var1} -> (({var1} -> {var2}) -> !!{var1}))",
                      "((!!{var1} -> (({var1} -> {var2}) -> !!{var1})) -> (!{var2} -> (!!{var1} -> (({var1} -> {var2}) -> !!{var1}))))",
                      "(!{var2} -> (!!{var1} -> (({var1} -> {var2}) -> !!{var1})))",
                      "((!{var2} -> !!{var1}) -> ((!{var2} -> (!!{var1} -> (({var1} -> {var2}) -> !!{var1}))) -> (!{var2} -> (({var1} -> {var2}) -> !!{var1}))))",
                      "((!{var2} -> (!!{var1} -> (({var1} -> {var2}) -> !!{var1}))) -> (!{var2} -> (({var1} -> {var2}) -> !!{var1})))",
                      "(!{var2} -> (({var1} -> {var2}) -> !!{var1}))",
                      "(!{var1} -> (!!{var1} -> !({var1} -> {var2})))",
                      "((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (!{var2} -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))",
                      "(!{var2} -> (!{var1} -> (!!{var1} -> !({var1} -> {var2}))))",
                      "((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))",
                      "(((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2}))))) -> (!{var2} -> ((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))))",
                      "(!{var2} -> ((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2}))))))",
                      "((!{var2} -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> ((!{var2} -> ((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))) -> (!{var2} -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))))",
                      "((!{var2} -> ((!{var1} -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))) -> (!{var2} -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2}))))))",
                      "(!{var2} -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))))",
                      "((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))",
                      "(((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))) -> (!{var2} -> ((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))))",
                      "((!{var2} -> (({var1} -> {var2}) -> !{var1})) -> ((!{var2} -> ((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> !{var1}) -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))",
                      "((!{var2} -> (({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2}))))) -> ((!{var2} -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))) -> (!{var2} -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> (!{var1} -> (!!{var1} -> !({var1} -> {var2})))) -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))) -> (!{var2} -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))))",
                      "(!{var2} -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))))",
                      "((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))",
                      "(((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2})))) -> (!{var2} -> ((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2})))))",
                      "((!{var2} -> (({var1} -> {var2}) -> !!{var1})) -> ((!{var2} -> ((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> !!{var1}) -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))) -> (!{var2} -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2})))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2}))))",
                      "((!{var2} -> (({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2})))) -> ((!{var2} -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2})))) -> (!{var2} -> (({var1} -> {var2}) -> !({var1} -> {var2})))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> (!!{var1} -> !({var1} -> {var2}))) -> (({var1} -> {var2}) -> !({var1} -> {var2})))) -> (!{var2} -> (({var1} -> {var2}) -> !({var1} -> {var2}))))",
                      "(!{var2} -> (({var1} -> {var2}) -> !({var1} -> {var2})))",
                      "!!({var1} -> {var2})",
                      "(!!({var1} -> {var2}) -> (!{var2} -> !!({var1} -> {var2})))",
                      "(!{var2} -> !!({var1} -> {var2}))",
                      "(!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2})))",
                      "((!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2}))) -> (!{var2} -> (!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2})))))",
                      "(!{var2} -> (!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2}))))",
                      "((!{var2} -> !!({var1} -> {var2})) -> ((!{var2} -> (!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2})))) -> (!{var2} -> (({var1} -> {var2}) -> !!({var1} -> {var2})))))",
                      "((!{var2} -> (!!({var1} -> {var2}) -> (({var1} -> {var2}) -> !!({var1} -> {var2})))) -> (!{var2} -> (({var1} -> {var2}) -> !!({var1} -> {var2}))))",
                      "(!{var2} -> (({var1} -> {var2}) -> !!({var1} -> {var2})))",
                      "((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))",
                      "(((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2}))) -> (!{var2} -> ((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2}))))",
                      "((!{var2} -> (({var1} -> {var2}) -> !({var1} -> {var2}))) -> ((!{var2} -> ((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))) -> (!{var2} -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> !({var1} -> {var2})) -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))) -> (!{var2} -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2}))))",
                      "(!{var2} -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2})))",
                      "((!{var2} -> (({var1} -> {var2}) -> !!({var1} -> {var2}))) -> ((!{var2} -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2}))) -> (!{var2} -> !({var1} -> {var2}))))",
                      "((!{var2} -> ((({var1} -> {var2}) -> !!({var1} -> {var2})) -> !({var1} -> {var2}))) -> (!{var2} -> !({var1} -> {var2})))",
                      "(!{var2} -> !({var1} -> {var2}))",
                      "(!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1}))",
                      "((!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1})) -> (!{var2} -> (!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1}))))",
                      "(!{var2} -> (!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1})))",
                      "((!{var2} -> !({var1} -> {var2})) -> ((!{var2} -> (!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1}))) -> (!{var2} -> (!!({var1} -> {var2}) -> !{var1}))))",
                      "((!{var2} -> (!({var1} -> {var2}) -> (!!({var1} -> {var2}) -> !{var1}))) -> (!{var2} -> (!!({var1} -> {var2}) -> !{var1})))",
                      "(!{var2} -> (!!({var1} -> {var2}) -> !{var1}))",
                      "((!{var2} -> !!({var1} -> {var2})) -> ((!{var2} -> (!!({var1} -> {var2}) -> !{var1})) -> (!{var2} -> !{var1})))",
                      "((!{var2} -> (!!({var1} -> {var2}) -> !{var1})) -> (!{var2} -> !{var1}))",
                      "(!{var2} -> !{var1})",
                      "((!{var2} -> !{var1}) -> ((!{var2} -> !!{var1}) -> !!{var2}))",
                      "((!{var2} -> !!{var1}) -> !!{var2})",
                      "!!{var2}"]


def get_modus_ponens_proof(var1, var2):
    r = []
    for line in modus_ponens_lemma:
        r.append(line.format(var1=var1, var2=var2))
    return r
