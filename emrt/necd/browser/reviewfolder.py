from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from esdrt.content import reviewfolder


class NECDReviewFolderView(reviewfolder.ReviewFolderView):
    index = ViewPageTemplateFile('./templates/necdreviewfolderview.pt')

    def __call__(self, *args, **kwargs):
        return self.index(self.context)