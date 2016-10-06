-ifndef(_thrift3214_types_included).
-define(_thrift3214_types_included, yeah).

%% struct 'StringMap'

-record('StringMap', {'data' = dict:from_list([{1,"a"},{2,"b"}]) :: dict()}).
-type 'StringMap'() :: #'StringMap'{}.

-endif.
