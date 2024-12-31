"""
    Interface to use localgradimportance.Importance without a model in hand; creates a SuperBasicNetwork
"""

def importance(
    X: np.ndarray | pd.DataFrame,
    Xk: np.ndarray | pd.DataFrame,
    y: np.ndarray | pd.Series,
    bandwidth: float | None = None,
    use_std: bool = True,
    exponent: float = 2.0,
    drop_first: bool = True,
    # SuperBasicNetworks Parameters
    save_root: str = '',
    save_name: str = '',
    epochs: int = 500,
    dense_activation: str = 'relu', # 'relu', 'sigmoid',...
    # Hyper parameters
    first_layer_width: float | int = 0.25, # int = absolute size, float = proportion of input
    layers: int = 2,
    layer_shrink_factor: float = 0.25,
    learning_rate: float = 0.01,
    verbose: int = 0
    ) -> np.ndarray:
    """
        Creates a SuperBasicNetwork and uses it for local grad importance
    """
    from . import SuperBasicNetworks
    from . import Importance
    
    network = SuperBasicNetworks.SimpleNN(
        save_root = save_root,
        save_name = save_name,
        epochs = epochs,
        dense_activation = dense_activation,
        first_layer_width = first_layer_width,
        layers = layers,
        layer_shrink_factor = layer_shrink_factor,
        learning_rate = learning_rate,
        verbose = verbose
    )
    
    return Importance.importanceFromModel(
        mode = network,
        X = X,
        Xk = Xk,
        y = y,
        bandwidth = bandwidth,
        use_std = use_std,
        exponent = exponent,
        drop_first = drop_first
    )
#/def importance