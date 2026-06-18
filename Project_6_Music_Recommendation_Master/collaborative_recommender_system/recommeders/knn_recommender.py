from sklearn.neighbors import NearestNeighbors
import numpy as np


def _fuzzy_ratio(s1, s2):
    """Simple fuzzy ratio replacement for fuzzywuzzy using difflib."""
    import difflib
    return int(difflib.SequenceMatcher(None, s1, s2).ratio() * 100)


class Recommender:
    def __init__(self, metric, algorithm, k, data, decode_id_song):
        self.metric = metric
        self.algorithm = algorithm
        self.k = k
        self.data = data
        self.decode_id_song = decode_id_song
        self.model = self._recommender().fit(data)

    def make_recommendation(self, new_song, n_recommendations):
        recommended = self._recommend(new_song=new_song, n_recommendations=n_recommendations)
        print("... Done")
        return recommended

    def _recommender(self):
        return NearestNeighbors(
            metric=self.metric,
            algorithm=self.algorithm,
            n_neighbors=self.k,
            n_jobs=-1
        )

    def _recommend(self, new_song, n_recommendations):
        recommendations = []
        recommendation_ids = self._get_recommendations(
            new_song=new_song, n_recommendations=n_recommendations
        )
        recommendations_map = self._map_indeces_to_song_title(recommendation_ids)
        for i, (idx, dist) in enumerate(recommendation_ids):
            recommendations.append(recommendations_map[idx])
        return recommendations

    def _get_recommendations(self, new_song, n_recommendations):
        recom_song_id = self._fuzzy_matching(song=new_song)
        if recom_song_id is None:
            return []
        print(f"Starting the recommendation process for {new_song} ...")
        distances, indices = self.model.kneighbors(
            self.data[recom_song_id], n_neighbors=n_recommendations + 1
        )
        return sorted(
            list(zip(indices.squeeze().tolist(), distances.squeeze().tolist())),
            key=lambda x: x[1]
        )[:0:-1]

    def _map_indeces_to_song_title(self, recommendation_ids):
        return {song_id: song_title for song_title, song_id in self.decode_id_song.items()}

    def _fuzzy_matching(self, song):
        match_tuple = []
        for title, idx in self.decode_id_song.items():
            ratio = _fuzzy_ratio(title.lower(), song.lower())
            if ratio >= 60:
                match_tuple.append((title, idx, ratio))
        match_tuple = sorted(match_tuple, key=lambda x: x[2])[::-1]
        if not match_tuple:
            print(f"The recommendation system could not find a match for {song}")
            return None
        return match_tuple[0][1]
