from collections import OrderedDict

def prototype_state():
    state = {}
    # Random seed
    state['seed'] = 1234
    # Logging level
    state['level'] = 'INFO'

    # A string representation for the unknown word placeholder for both language
    state['oov'] = '<unk>'
    state['unk_sym'] = 0
    state['start_sym_query'] = '<q>'
    state['end_sym_query'] = '</q>'
    state['end_sym_session'] = '</s>'

    # Low-rank approximation activation function
    state['rank_n_activ'] = 'lambda x: x'
    # Hidden-to-hidden activation function
    state['activ'] = 'lambda x: TT.tanh(x)'

    # Dimensionality of hidden layers
    state['qdim'] = 512
    # Dimensionality of session hidden layer
    state['sdim'] = 1024
    # Dimensionality of low-rank approximation
    state['rankdim'] = 256
    state['lambda_rank'] = 0.

    # Threshold to clip the gradient
    state['cutoff'] = 1.
    state['lr'] = 0.0001

    # Early stopping configuration
    state['patience'] = 5
    state['cost_threshold'] = 1.003

    # Choose optimization algorithm
    state['updater'] = 'adam'
    # Batch size
    state['bs'] = 80
    state['decoder_bias_type'] = 'first'
    # We take this many minibatches, merge them,
    # sort the sentences according to their length and create
    # this many new batches with less padding.
    state['sort_k_batches'] = 20
    # Maximum sequence length / trim batches
    state['seqlen'] = 60
    # Should we use a deep output layer
    # and maxout on the outputs?
    state['deep_out'] = True
    state['maxout_out'] = False
    state['use_nce'] = False
    state['save_dir'] = './'
    # Frequency of training error reports (in number of batches)
    state['train_freq'] = 10
    # Validation frequency
    state['valid_freq'] = 5000
    # Number of batches to process
    state['loop_iters'] = 3000000
    # Maximum number of minutes to run
    state['time_stop'] = 24*60*31
    # Error level to stop at
    state['minerr'] = -1
    return state

def prototype_test():
    state = prototype_state()

    state['train_session'] = "/data/disk1/private/wubin/hred-qs/data_s/train.ses.pkl"
    state['train_rank'] = "/data/disk1/private/wubin/hred-qs/data_s/train.rnk.pkl"
    state['valid_session'] = "/data/disk1/private/wubin/hred-qs/data_s/valid.ses.pkl"
    state['valid_rank'] = "/data/disk1/private/wubin/hred-qs/data_s/valid.rnk.pkl"
    state['dictionary'] = "/data/disk1/private/wubin/hred-qs/data_s/train.dict.pkl"
    state['save_dir'] = '/data/disk1/private/wubin/hred-qs/models_s/'
    state['decoder_bias_type'] = 'first'
    state['prefix'] = "test"
    state['deep_out'] = False
    state['maxout_out'] = False
    state['updater'] = 'adam'
    state['lambda_rank'] = 0.
    state['use_nce'] = False

    state['qdim'] = 128
    # Dimensionality of session hidden layer
    state['sdim'] = 256
    # Dimensionality of low-rank approximation
    state['rankdim'] = 64

    state['bs'] = 5 
    state['seqlen'] = 15
    state['eos_sym'] = 2
    state['eoq_sym'] = 1

    state['session_rec_activation'] = "lambda x: T.tanh(x)"
    state['query_rec_activation'] = "lambda x: T.tanh(x)"

    state['session_step_type'] = 'plain'
    state['query_step_type'] = 'plain'
    return state

def aol_path():
    state = prototype_state()
    state['dictionary'] = "/data/disk1/private/wubin/hred-qs/data_s/train.dict.pkl"
    state['train_session'] = "/data/disk1/private/wubin/hred-qs/data_s/train.ses.pkl"
    state['train_rank'] = "/data/disk1/private/wubin/hred-qs/data_s/train.rnk.pkl"
    state['valid_session'] = "/data/disk1/private/wubin/hred-qs/data_s/valid.ses.pkl"
    state['valid_rank'] = "/data/disk1/private/wubin/hred-qs/data_s/valid.rnk.pkl"
    return state

def aol():
    state = aol_path()
    state['maxout_out'] = False
    state['deep_out'] = True
    state['use_nce'] = False
    state['updater'] = 'adam'
    state['lambda_rank'] = 0.0
    state['valid_freq'] = 5000

    # Dimensionality of the query hidden layer
    state['qdim'] = 400
    # Dimensionality of session hidden layer
    state['sdim'] = 800
    # Dimensionality of low-rank approximation
    state['rankdim'] = 200
    state['bs'] = 1
    state['seqlen'] = 30
    state['eos_sym'] = 2
    state['eoq_sym'] = 1
    state['save_dir'] = './wb/models_s/'
    state['session_rec_activation'] = "lambda x: T.tanh(x)"
    state['query_rec_activation'] = "lambda x: T.tanh(x)"
    state['session_step_type'] = "gated"
    state['query_step_type'] = "gated"
    return state
