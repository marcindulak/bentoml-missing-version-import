from bentoml import api, env, artifacts, BentoService
from bentoml.adapters import StringInput, JsonOutput
from bentoml.frameworks.sklearn import SklearnModelArtifact

from mypackage._version import __version__


@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact("model")])
class Service(BentoService):

    @api(input=StringInput(), output=JsonOutput())
    def say_hi(self, x):
        return f"Hello {x}!"

from sklearn.svm import SVC

class MySVC(SVC):
    pass

