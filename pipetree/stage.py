# MIT License

# Copyright (c) 2016 Morgan McDermott & John Carlyle

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from pipetree.storage import LocalFileArtifactProvider
from pipetree.exceptions import InvalidConfigurationFileError


class BasePipelineStage(object):
    """Base class for a pipeline stage"""
    def __init__(self, config):
        if self._validate_config(config):
            self._config = config

    @property
    def name(self):
        return self._config.name

    def __source_artifact(self, artifact_name):
        raise NotImplementedError

    def __yield_artifacts(self):
        raise NotImplementedError

    def _validate_config(self):
        raise NotImplementedError


class LocalDirectoryPipelineStage(BasePipelineStage):
    """A pipeline stage for sourcing files from a directory"""

    def __init__(self, config):
        super().__init__(config)
        self._artifact_source = LocalFileArtifactProvider(config.filepath)

    def __source_artifact(self, artifact_name):
        pass

    def __yield_artifacts(self):
        pass

    def _validate_config(self, config):
        """
        Raise an exception if the config is invald
        """
        if not hasattr(config, 'filepath'):
            raise InvalidConfigurationFileError(
                configurable=self.__class__.__name__,
                reason='expected \'filepath\' entry of type string.')
        return True


class PipelineStageFactory(object):
    def create_pipeline_stage(self, pipeline_config):
        stage = self._create_pipeline_stage_class(pipeline_config)
        return stage

    def _create_pipeline_stage_class(self, pipeline_config):
        class_attributes = self._generate_attributes(pipeline_config)
        parent_class = tuple([pipeline_config.parent_class])
        class_name = pipeline_config.name
        cls = type(class_name, parent_class, class_attributes)
        return cls(pipeline_config)

    def _generate_attributes(self, config):
        return {}
