from django.contrib import admin
from .models import Video, Frame, TEvent, IndexEntries, QueryResults, DVAPQL, \
    Region, Tube, Segment, DeletedVideo, \
    RegionLabel, TubeLabel, Label, ManagementAction, \
    TrainedModel, Retriever, SystemState, Worker, QueryRegion, QueryRegionIndexVector, \
    QueryRegionResults, TrainingSet, Export, TaskRestart, RegionRelation


@admin.register(RegionRelation)
class RegionRelationAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskRestart)
class TaskRestartAdmin(admin.ModelAdmin):
    pass


@admin.register(Export)
class ExportAdmin(admin.ModelAdmin):
    pass


@admin.register(SystemState)
class SystemStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionLabel)
class RegionLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(TubeLabel)
class TubeLabelAdmin(admin.ModelAdmin):
    pass


@admin.register(Segment)
class SegmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(DeletedVideo)
class DeletedVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryResults)
class QueryResultsAdmin(admin.ModelAdmin):
    pass


@admin.register(DVAPQL)
class DVAPQLAdmin(admin.ModelAdmin):
    pass

@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass


@admin.register(IndexEntries)
class IndexEntriesAdmin(admin.ModelAdmin):
    pass


@admin.register(TEvent)
class TEventAdmin(admin.ModelAdmin):
    pass


@admin.register(Tube)
class TubeAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainedModel)
class TrainedModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Retriever)
class RetrieverAdmin(admin.ModelAdmin):
    pass


@admin.register(ManagementAction)
class ManagementActionAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryRegion)
class QueryRegionAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryRegionIndexVector)
class QueryRegionIndexVectorAdmin(admin.ModelAdmin):
    pass


@admin.register(QueryRegionResults)
class QueryRegionResultsAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingSet)
class TrainingSetAdmin(admin.ModelAdmin):
    pass
