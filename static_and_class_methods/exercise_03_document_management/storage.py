from static_and_class_methods.exercise_03_document_management.category import Category
from static_and_class_methods.exercise_03_document_management.document import Document
from static_and_class_methods.exercise_03_document_management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_to_edit = next(filter(lambda c: c.id == category_id, self.categories))
        category_to_edit.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = next(filter(lambda t: t.id == topic_id, self.topics))
        topic_to_edit.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document_to_edit = next(filter(lambda d: d.id == document_id, self.documents))
        document_to_edit.edit(new_file_name)

    def delete_topic(self, topic_id: int):
        self.topics = [topic for topic in self.topics if topic.id != topic_id]

    def delete_document(self, document_id: int):
        self.documents = [document for document in self.documents if document.id != document_id]

    def delete_category(self, category_id: int):
        self.categories = [category for category in self.categories if category.id != category_id]

    def get_document(self, document_id: int):
        return next(filter(lambda d: d.id == document_id, self.documents))

    def __repr__(self):
        return "\n".join(str(doc) for doc in self.documents)
